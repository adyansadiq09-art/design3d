import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="dev",
    password="dev123",
    database="design3d"
)

if conn.is_connected():
    print("Connected to MySQL!")

cursor = conn.cursor()
cursor.execute("SELECT DATABASE()")
print("Using database:", cursor.fetchone()[0])

cursor.close()
conn.close()