import sqlite3

conn = sqlite3.connect("sahayak.db")
cursor = conn.cursor()

cursor.execute("DELETE FROM contacts")
cursor.execute("DELETE FROM sys_command")
cursor.execute("DELETE FROM web_command")

conn.commit()

print("Database cleaned successfully!")

conn.close()