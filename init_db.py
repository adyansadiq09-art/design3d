import mysql.connector

conn = mysql.connector.connect(
    host="localhost", user="dev", password="dev123", database="design3d"
)
cursor = conn.cursor()

with open("schema.sql") as f:
    sql = f.read()

for statement in sql.split(";"):
    if statement.strip():
        cursor.execute(statement)

conn.commit()

cursor.execute("SHOW TABLES")
for (table,) in cursor.fetchall():
    print("Table:", table)

cursor.close()
conn.close()