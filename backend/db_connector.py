import mysql.connector
from os import getenv

MYSQL_HOST = getenv("MYSQL_HOST")
MYSQL_USER = getenv("MYSQL_USER")
MYSQL_PASSWORD = getenv("MYSQL_PASSWORD")
MYSQL_DB = getenv("MYSQL_DB")

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