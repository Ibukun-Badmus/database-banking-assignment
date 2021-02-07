import mysql.connector
from mysql.connector import Error

customerId = input("CustomerId")
firstname = input("Customer name")
lastname = input("Customer name")
middlename = input("Customer name")
dateofbirth = input("dob")
mobile = int(input("number"))
occupation = input("occupation")

accountnumber = int(input("Enter account number"))
accounttype = input("Enter the accountType")
accountstatus = input("Enter the accountstatus")
accountopeningdate = input("enter the account opening date")

transactionid = int(input("Enter the transaction id"))
transactiondate = input("Enter the transaction date")
transactiontype = input("Enter the transaction type")
amount = input("Enter the transaction amount")
transactionmedium = input("Enter the transaction medium")


def connect_insert_into_banking():
    conn = None
    try:
        conn = mysql.connector.connect(host='localhost',
                                       database='Banking',
                                       user='Ibukun',
                                       password='oluwaibukun')
        print("connected to the database")
        if conn.is_connected():
            print("connected to database")
        db_cursor = conn.cursor()
        sql = "INSERT INTO customers (customerId,firstName,lastName,middleName,dateOfBirth,mobileNumber,occupation)" \
              " values (%s,%s,%s,%s,%s,%s,%s)"
        val = [customerId, firstname, lastname, middlename, dateofbirth, mobile, occupation]

        db_cursor.execute(sql, val)
        conn.commit()
        print(db_cursor.rowcount, "row was counted")
        db_cursor.close()
    except Error as e:
        print('error ', e)
    finally:
        conn.close()


def connect_insert_into_account():
    conn = None
    try:
        conn = mysql.connector.connect(host='localhost',
                                       database='Banking',
                                       user='Ibukun',
                                       password='oluwaibukun')
        print("connected to the database")
        if conn.is_connected():
            print("connected to database")
        db_cursor = conn.cursor()
        sql = "INSERT INTO account (accountNumber, customerId, accountType, accountStatus, accountOpeningDate)values (%s,%s,%s,%s,%s)"
        val = [accountnumber, customerId, accounttype, accountstatus, accountopeningdate]

        db_cursor.execute(sql, val)
        conn.commit()
        print(db_cursor.rowcount, "row was counted")
        db_cursor.close()
    except Error as e:
        print('error ', e)
    finally:
        conn.close()


def connect_insert_into_transaction():
    conn = None
    try:
        conn = mysql.connector.connect(host='localhost',
                                       database='Banking',
                                       user='Ibukun',
                                       password='oluwaibukun')
        print("connected to the database")
        if conn.is_connected():
            print("connected to database")
        db_cursor = conn.cursor()
        sql = "INSERT INTO transaction(transactionId,accountNumber,transaction_Date,transaction_Type,amount,transaction_medium)values (%s,%s,%s,%s,%s,%s)"
        val = [transactionid, accountnumber, transactiondate, transactiontype, amount, transactionmedium]

        db_cursor.execute(sql, val)
        conn.commit()
        print(db_cursor.rowcount, "row was counted")
        db_cursor.close()
    except Error as e:
        print('error ', e)
    finally:
        conn.close()


connect_insert_into_banking()
connect_insert_into_account()
connect_insert_into_transaction()
