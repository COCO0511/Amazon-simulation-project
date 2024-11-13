import psycopg2

def connect_db():
    try:
        conn = psycopg2.connect(host = "db", database = "postgres", user = "postgres", password = "postgres", port = "5432")
        return (conn, conn.cursor())
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

def exec_db(sql, conn, cursor):
    cursor.execute(sql)
    conn.commit()
    
def disconnect_db(conn):
    conn.close()
    