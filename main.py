import sqlite3


# crear una conexion
con = sqlite3.connect('base.db')
# crear un cursor (o tambien llamado comando)
cursor = con.cursor()

cursor.close()

con.close()

