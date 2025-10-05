import sqlite3

conn = sqlite3.connect("site.db")
cursor = conn.cursor()

# Show all tables
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
print("Tables:", cursor.fetchall())

# Fetch all rows from the 'todo' table
try:
    cursor.execute("SELECT * FROM todo;")  # table name matches your model
    rows = cursor.fetchall()
    print("\nData in todo table:")
    for row in rows:
        print(row)
except Exception as e:
    print("Error:", e)

conn.close()