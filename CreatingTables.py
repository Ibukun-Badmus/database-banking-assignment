
import mysql.connector
from mysql.connector import Error


def create_tables():
    conn = None
    try:
        conn = mysql.connector.connect(
            host='localhost',
            user='Ibukun',
            password='oluwaibukun',
            database='Banking'
        )
        mydb = conn.cursor()
        customer = "CREATE TABLE customers(customerId varchar(20) primary key," \
                   " firstName VARCHAR(30) Not null," \
                   "lastName varchar(30) not null," \
                   "middleName varchar (30) not null," \
                   "dateOfBirth DATE," \
                   "mobileNumber int not null ," \
                   "occupation varchar (20))"
        account = "CREATE TABLE account(accountNumber INT  UNIQUE primary key," \
                  "customerId varchar(20) ," \
                  "accountType varchar(30)," \
                  "accountStatus varchar(30)," \
                  "accountOpeningDate DATE," \
                  "FOREIGN key (customerId) references customers(customerId))"
        transaction = "CREATE TABLE transaction (transactionId INT PRIMARY KEY," \
                      "accountNumber INT," \
                      "transaction_Date DATE ," \
                      "transaction_Type varchar(30)," \
                      "amount int," \
                      "transaction_medium varchar (30)," \
                      "FOREIGN key (accountNumber) references account(accountNumber)" \
                      ")"
        mydb.execute(customer)
        mydb.execute(account)
        mydb.execute(transaction)
        if conn.connect():
            print("Connected to the database")
    except Error as e:
        print('Not connecting due to: ', e)
    finally:
        if conn is not None and conn.is_connected():
            conn.close()
            print('database shutdown!!')


def main():
    create_tables()


if __name__ == '__main__':
    main()
