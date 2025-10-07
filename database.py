# 📁 database.py
# Handles SQLite connection, table creation, and helper functions for Course Management

import sqlite3

DB_NAME = "courses.db"

def get_connection():
    return sqlite3.connect(DB_NAME)

def init_db():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS courses (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        semester TEXT NOT NULL
    )
    """)

    cur.execute("""
    CREATE TABLE IF NOT EXISTS categories (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        course_id INTEGER,
        name TEXT NOT NULL,
        points REAL NOT NULL,
        FOREIGN KEY(course_id) REFERENCES courses(id)
    )
    """)

    cur.execute("""
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        course_id INTEGER,
        first TEXT NOT NULL,
        last TEXT NOT NULL,
        FOREIGN KEY(course_id) REFERENCES courses(id)
    )
    """)

    cur.execute("""
    CREATE TABLE IF NOT EXISTS scores (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        student_id INTEGER,
        category_id INTEGER,
        earned_points REAL NOT NULL,
        FOREIGN KEY(student_id) REFERENCES students(id),
        FOREIGN KEY(category_id) REFERENCES categories(id)
    )
    """)

    conn.commit()
    conn.close()

def insert_course(name, semester):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("INSERT INTO courses (name, semester) VALUES (?, ?)", (name, semester))
    conn.commit()
    course_id = cur.lastrowid
    conn.close()
    return course_id

def insert_category(course_id, name, points):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("INSERT INTO categories (course_id, name, points) VALUES (?, ?, ?)", (course_id, name, points))
    conn.commit()
    conn.close()

def insert_student(course_id, first, last):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("INSERT INTO students (course_id, first, last) VALUES (?, ?, ?)", (course_id, first, last))
    conn.commit()
    student_id = cur.lastrowid
    conn.close()
    return student_id

def insert_score(student_id, category_id, earned_points):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("INSERT INTO scores (student_id, category_id, earned_points) VALUES (?, ?, ?)", 
                (student_id, category_id, earned_points))
    conn.commit()
    conn.close()
