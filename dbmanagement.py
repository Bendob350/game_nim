from mysql import connector
import json

DB_CFG = { 'host':'127.0.0.1','user':'root','password':'Mohamed.2005','database':'nimdb' }

def get_conn():
    return connector.connect(**DB_CFG)

def save_finished_game(p1_type, p2_type, winner_slot):
    sql = "INSERT INTO games (player1_type, player2_type, winner) VALUES (%s,%s,%s)"
    with get_conn() as db, db.cursor() as cur:
        cur.execute(sql, (p1_type, p2_type, winner_slot))
        db.commit()

def save_unfinished_game(p1_type, p2_type, current_player, piles):
    state = json.dumps({'piles':piles})
    sql = "INSERT INTO saved_games (player1_type,player2_type,current_player,state) VALUES (%s,%s,%s,%s)"
    with get_conn() as db, db.cursor() as cur:
        cur.execute(sql, (p1_type,p2_type,current_player,state))
        db.commit()

def load_last_unfinished():
    sql = "SELECT player1_type,player2_type,current_player,state FROM saved_games ORDER BY id DESC LIMIT 1"
    with get_conn() as db, db.cursor() as cur:
        cur.execute(sql)
        row=cur.fetchone()
    if not row: return None
    p1,p2,curr,jsonstr = row
    return p1, p2, curr, json.loads(jsonstr)['piles']

def clear_saved_games():
    db = get_conn()
    cur = db.cursor()
    cur.execute("DELETE FROM saved_games ;")
    db.commit()

def clear_finished_games():
    db = get_conn()
    cur = db.cursor()
    cur.execute("DELETE FROM games ;")
    db.commit()