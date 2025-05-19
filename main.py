from mysql import connector
from dao import * 

def get_connection():
    return connector.connect(
        user='root',
        password='',
        database='db_game',
        host='127.0.0.1',
        port=3306
        )

if __name__ == "__main__":
    try:
        con = get_connection()
        create_player('player1', con)
        get_players(con)
    except Exception as e:
        print(e)
