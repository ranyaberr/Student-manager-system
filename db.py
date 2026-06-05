import sqlite3

conn = sqlite3.connect("students.db")
cursor = conn.cursor()