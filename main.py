from mysql import connector

def get_connection():
    return connector.connect(
        user='root',
        password='',
        database='db_game',
        host='127.0.0.1',
        port=3306
        )

def create_player(player):
    query = "insert into t_player (name) values (%s)"
    try :
        con=get_connection()
        cursor = con.cursor()
        cursor.execute(query,player)
        con.commit()
    except Exception as e:
        print(e)

def get_players():
    query = "SELECT * FROM t_player"
    try :
        con=get_connection()
        cursor = con.cursor()
        cursor.execute(query)
        print(cursor.fetchall())
    except Exception as e:
        print(e)

def update(name,new_player):
    pass

def delete(name):
    pass

if __name__ == "__main__":
    get_players()
