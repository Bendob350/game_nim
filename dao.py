def create_player(player,con):
    query = "insert into t_player (name) values (%s)"
    try :
        cursor = con.cursor()
        cursor.execute(query,(player,))
        con.commit()
    except Exception as e:
        if con:
            con.rollback()
        print(e)

def insert_info(table,champs,values,con):
    query = "insert into " +table +" "+champs+" values "+values
    #insert_info("t_bonus","(year,number,total)","('2023','1',100)",con)
    try :
        cursor = con.cursor()
        cursor.execute(query)
        con.commit()
    except Exception as e:
        if con:
            con.rollback()
        print(e)

def create_table (table,champs,con):
    query = "create table if not exists "+ table +" "+ champs
    # champs = "(year varchar(10),number varchar(10), total int "
    # table = "t_bonus"
    try :
        cursor = con.cursor()
        cursor.execute(query)
        con.commit()
    except Exception as e:
        if con:
            con.rollback()
        print(e)

def get_players(con):
    query = "SELECT * FROM t_player"
    try :
        cursor = con.cursor(dictionary=True)
        cursor.execute(query)
        print(cursor.fetchall())
    except Exception as e:
        print(e)
def get_player_by_name(player,con):
    query = "SELECT * FROM t_player WHERE name = %s"
    try :
        cursor = con.cursor()
        cursor.execute(query,(player,))
        return cursor.fetchall()[0]
    except Exception as e:
        print(e)

def load(data,con) :
    query = "insert into t_player (name) values (%s)"
    try :
        cursor = con.cursor()
        cursor.execute(query,data)
        con.commit()
    except Exception as e:
        if con:
            con.rollback()
        print(e)

def update(name,new_player,con):
    pass

def delete(name,con):
    pass