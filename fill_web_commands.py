import sqlite3

conn = sqlite3.connect("sahayak.db")
cursor = conn.cursor()

commands = [
    ("google", "https://www.google.com"),
    ("youtube", "https://www.youtube.com"),
    ("gmail", "https://mail.google.com"),
    ("github", "https://github.com"),
    ("instagram", "https://www.instagram.com"),
    ("linkedin", "https://www.linkedin.com"),
    ("chatgpt", "https://chatgpt.com"),
    ("whatsapp", "https://web.whatsapp.com"),
    ("spotify", "https://open.spotify.com"),
    ("google drive", "https://drive.google.com")
]

cursor.executemany(
    "INSERT INTO web_command (name, url) VALUES (?, ?)",
    commands
)

conn.commit()

print("Web commands added successfully!")

conn.close()

import sqlite3

conn = sqlite3.connect("sahayak.db")
cursor = conn.cursor()

cursor.execute("SELECT * FROM web_command")

for row in cursor.fetchall():
    print(row)

conn.close()