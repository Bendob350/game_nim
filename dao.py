def create_player(player,con):
    query = "insert into t_player (name) values (%s)"
    try :
        cursor = con.cursor()
        cursor.execute(query,player)
        con.commit()
    except Exception as e:
        if con:
            con.rollback()
        print(e)

def get_players(con):
    query = "SELECT * FROM t_player"
    try :
        cursor = con.cursor()
        cursor.execute(query)
        print(cursor.fetchall())
    except Exception as e:
        print(e)

def update(name,new_player,con):
    pass

def delete(name,con):
    pass