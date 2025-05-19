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
        name= 'player1'
        if get_player_by_name(name,con) == None : create_player(name, con)
        data = [('player1',), ('player2',), ('player3',)]
        load(data, con)
        get_players(con)
    except Exception as e:
        print(e)


""" les structures de données | la partie fichier"""