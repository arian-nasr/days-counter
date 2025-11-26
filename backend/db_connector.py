import mysql.connector
from os import getenv

MYSQL_HOST = getenv("MYSQL_HOST")
MYSQL_USER = getenv("MYSQL_USER")
MYSQL_PASSWORD = getenv("MYSQL_PASSWORD")
MYSQL_DB = getenv("MYSQL_DATABASE")

def db_create_table_if_not_exists():
    conn = mysql.connector.connect(
        host=MYSQL_HOST,
        user=MYSQL_USER,
        password=MYSQL_PASSWORD,
        database=MYSQL_DB
    )
    cursor = conn.cursor()
    create_table_query = """
    CREATE TABLE IF NOT EXISTS days (
        date DATE PRIMARY KEY,
        value INT NOT NULL
    )
    """
    cursor.execute(create_table_query)
    conn.commit()
    cursor.close()
    conn.close()

def db_get_day(date_str):
    conn = mysql.connector.connect(
        host=MYSQL_HOST,
        user=MYSQL_USER,
        password=MYSQL_PASSWORD,
        database=MYSQL_DB
    )
    cursor = conn.cursor(dictionary=True)
    query = "SELECT date, value FROM days WHERE date = %s"
    cursor.execute(query, (date_str,))
    result = cursor.fetchone()
    cursor.close()
    conn.close()
    return result