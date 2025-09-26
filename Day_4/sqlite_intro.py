from fastapi import FastAPI
from pydantic import BaseModel
import sqlite3

app = FastAPI()

# --- Database setup ---
def init_db():
    conn = sqlite3.connect("mydatabase.db")
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS tasks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        status TEXT NOT NULL
    )
    """)

    # sample data
    cursor.execute("INSERT INTO tasks (name, status) VALUES (?, ?)", ("Buy groceries", "pending"))
    cursor.execute("INSERT INTO tasks (name, status) VALUES (?, ?)", ("Write report", "completed"))
    cursor.execute("INSERT INTO tasks (name, status) VALUES (?, ?)", ("Clean room", "pending"))

    conn.commit()
    conn.close()

def get_db_connection():
    conn = sqlite3.connect("mydatabase.db")
    conn.row_factory = sqlite3.Row
    return conn

init_db()

# --- Pydantic model ---
class Task(BaseModel):
    name: str
    status: str  # "completed" or "pending"

# --- Endpoints ---

# Read tasks
@app.get("/tasks")
def read_tasks(status: str | None = None):
    conn = get_db_connection()
    cursor = conn.cursor()
    if status:
        cursor.execute("SELECT * FROM tasks WHERE status = ?", (status,))
    else:
        cursor.execute("SELECT * FROM tasks")
    rows = cursor.fetchall()
    conn.close()
    return [dict(row) for row in rows]

# Create a new task
@app.post("/tasks")
def create_task(task: Task):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO tasks (name, status) VALUES (?, ?)", (task.name, task.status))
    conn.commit()
    conn.close()
    return {"status": "success", "task": task}