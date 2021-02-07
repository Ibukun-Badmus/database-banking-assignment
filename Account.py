import mysql.connector
from mysql.connector import Error


def create_schema():
    conn = None
    try:
        conn = mysql.connector.connect(
            host='localhost',
            user='Ibukun',
            password='oluwaibukun'
        )
        mydb = conn.cursor()
        mydb.execute("CREATE Database Banking")

        if conn.connect():
            print("Connected to the database")
    except Error as e:
        print('Not connecting due to: ', e)
    finally:
        if conn is not None and conn.is_connected():
            conn.close()
            print('database shutdown!!')


def main():
    create_schema()


if __name__ == '__main__':
    main()
