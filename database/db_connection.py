import mysql.connector
import pandas as pd

# ------------------ LOAD BOOKS FROM MYSQL ------------------
def load_books_from_mysql():
    # Connect to MySQL (phpMyAdmin uses this same connection)
    conn = mysql.connector.connect(
        host="localhost",
        user="root",              # same user as in phpMyAdmin
        password="",              # leave blank if no password
        database="library_db"     # your database name
    )

    # Load data from the 'books' table
    query = "SELECT title, author, description FROM books;"
    df = pd.read_sql(query, conn)
    conn.close()
    return df


# ------------------ GET MYSQL CONNECTION ------------------
def get_db():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="library_db"
    )
    return conn
