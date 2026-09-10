'''import sqlite3

conn = sqlite3.connect("sahayak.db")
cursor = conn.cursor()

commands = [
    ("calculator", "calc.exe"),
    ("notepad", "notepad.exe"),
    ("paint", "mspaint.exe"),
    ("command prompt", "cmd.exe"),
    ("file explorer", "explorer.exe"),
    ("vs code", "code")
]

cursor.executemany(
    "INSERT INTO sys_command (name, path) VALUES (?, ?)",
    commands
)

conn.commit()

print("System commands added successfully!")

conn.close()
'''

import sqlite3

conn = sqlite3.connect("sahayak.db")
cursor = conn.cursor()

cursor.execute("SELECT * FROM sys_command")

for row in cursor.fetchall():
    print(row)

conn.close()