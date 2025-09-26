from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional
import sqlite3

app = FastAPI()

# --- Database setup ---
def init_db():
    conn = sqlite3.connect("mydatabase.db")
    cursor = conn.cursor()
    cursor.execute("DROP TABLE IF EXISTS books")
    cursor.execute("""
    CREATE TABLE books (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        price INTEGER NOT NULL,
        stock INTEGER NOT NULL,
        orders INTEGER NOT NULL
    )
    """)
    cursor.execute("INSERT INTO books (name, price, stock, orders) VALUES (?, ?, ?, ?)", ("Book A", 100, 50, 10))
    cursor.execute("INSERT INTO books (name, price, stock, orders) VALUES (?, ?, ?, ?)", ("Book B", 200, 20, 5))
    cursor.execute("INSERT INTO books (name, price, stock, orders) VALUES (?, ?, ?, ?)", ("Book C", 150, 10, 2))
    conn.commit()
    conn.close()

def get_db_connection():
    try:
        conn = sqlite3.connect("mydatabase.db")
        conn.row_factory = sqlite3.Row
        return conn
    except sqlite3.Error as e:
        raise HTTPException(status_code=500, detail=f"Database connection error: {e}")

init_db()


class BookCreate(BaseModel):
    name: str
    price: int
    stock: int
    orders: int

class Book(BaseModel):
    name: Optional[str] = None
    price: Optional[int] = None
    stock: Optional[int] = None
    orders: Optional[int] = None


# Read 
@app.get("/books")
def read_books():
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM books")
        rows = cursor.fetchall()
        conn.close()
        return [dict(row) for row in rows]
    except sqlite3.Error as e:
        raise HTTPException(status_code=500, detail=f"Database error: {e}")

# Create 
@app.post("/books")
def create_book(book: BookCreate):
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO books (name, price, stock, orders) VALUES (?, ?, ?, ?)",
            (book.name, book.price, book.stock, book.orders)
        )
        conn.commit()
        new_id = cursor.lastrowid
        conn.close()
        return {"status": "success", "book_id": new_id, "book": book}
    except sqlite3.IntegrityError:
        raise HTTPException(status_code=400, detail="Invalid input: All fields are required")
    except sqlite3.Error as e:
        raise HTTPException(status_code=500, detail=f"Database error: {e}")

# Update 
@app.put("/books/{book_id}")
def update_book(book_id: int, book: Book):
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM books WHERE id = ?", (book_id,))
        existing_book = cursor.fetchone()
        if existing_book is None:
            conn.close()
            raise HTTPException(status_code=404, detail="Book not found")

        fields = []
        values = []
        if book.name is not None:
            fields.append("name = ?")
            values.append(book.name)
        if book.price is not None:
            fields.append("price = ?")
            values.append(book.price)
        if book.stock is not None:
            fields.append("stock = ?")
            values.append(book.stock)
        if book.orders is not None:
            fields.append("orders = ?")
            values.append(book.orders)

        if not fields:
            conn.close()
            raise HTTPException(status_code=400, detail="No fields provided to update")

        values.append(book_id)
        query = f"UPDATE books SET {', '.join(fields)} WHERE id = ?"
        cursor.execute(query, values)
        conn.commit()
        conn.close()

        return {"status": "success", "book_id": book_id, "updated_fields": [f.split(' = ')[0] for f in fields]}
    except sqlite3.Error as e:
        raise HTTPException(status_code=500, detail=f"Database error: {e}")

# Delete 
@app.delete("/books/{book_id}")
def delete_book(book_id: int):
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM books WHERE id = ?", (book_id,))
        conn.commit()
        deleted = cursor.rowcount
        conn.close()
        if deleted == 0:
            raise HTTPException(status_code=404, detail="Book not found")
        return {"status": "success", "book_id": book_id}
    except sqlite3.Error as e:
        raise HTTPException(status_code=500, detail=f"Database error: {e}")