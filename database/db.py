# database/db.py
import sqlite3

DB_NAME = "database/progress.db"


def init_db():

    conn = sqlite3.connect(DB_NAME)

    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS student_progress(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        topic TEXT,
        score INTEGER,
        total INTEGER,
        percentage REAL,
        level TEXT
    )
    """)

    conn.commit()
    conn.close()


def save_result(topic, result):

    conn = sqlite3.connect(DB_NAME)

    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO student_progress
    (
        topic,
        score,
        total,
        percentage,
        level
    )
    VALUES (?, ?, ?, ?, ?)
    """,
    (
        topic,
        result["score"],
        result["total"],
        result["percentage"],
        result["level"]
    ))

    conn.commit()
    conn.close()


def get_progress():

    conn = sqlite3.connect(DB_NAME)

    cursor = conn.cursor()

    cursor.execute("""
    SELECT *
    FROM student_progress
    """)

    data = cursor.fetchall()

    conn.close()

    return data