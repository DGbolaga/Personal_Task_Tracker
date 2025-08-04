import sqlite3
import os

db_dir = os.path.join(os.path.dirname(__file__), '..', 'data')
os.makedirs(db_dir, exist_ok=True)

# Define DB file path
db_path = os.path.join(db_dir, 'tasks.db')

conn = sqlite3.connect(db_path)
cursor = conn.cursor()


#id, description, status, added_date, due_date, priority
# Create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    description TEXT NOT NULL,
    status TEXT NOT NULL,
    added_date TEXT NOT NULL,
    due_date TEXT, 
    priority TEXT NOT NULL                              
)
""")

conn.commit()
conn.close()    

print(f'Database created at {db_path}')
