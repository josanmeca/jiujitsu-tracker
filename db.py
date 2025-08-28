import sqlite3

DB_NAME = "jiujitsu.db"

def get_connection():
    return sqlite3.connect(DB_NAME)

def create_tables():
    conn = get_connection()
    cursor = conn.cursor()
    with open("models.sql", "r") as f:
        cursor.executescript(f.read())
    conn.commit()
    conn.close()

def add_session(fecha, tipo, duracion, sensaciones):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO sessions (fecha, tipo, duracion, sensaciones) VALUES (?, ?, ?, ?)",
        (fecha, tipo, duracion, sensaciones),
    )
    conn.commit()
    conn.close()

def get_all_sessions():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM sessions")
    rows = cursor.fetchall()
    conn.close()
    return rows

def delete_session(session_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM sessions WHERE id = ?", (session_id,))
    conn.commit()
    conn.close()
