# 🧠 Course Management System (SQL Edition)

A fully interactive, object-oriented Python console application that simulates a simple course management system — now powered by **SQLite** for persistent data storage.  

This program allows users to:

- Create courses with validated **two-word names** (e.g., “CIS 325”)  
- Define grading categories using **1–5 letter acronyms**  
- Input and validate **semester names** (e.g., “Fall 2025”)  
- Enroll students with proper **first + last name validation**  
- Enter and store scores in a **SQLite database**  
- Display a complete course roster with scores for each student, even after restarting the program

This upgrade demonstrates strong **Python fundamentals**, **object-oriented programming**, and **database integration**, making it an excellent portfolio piece for IT/programming roles.

---

## ▶️ How to Run

```bash
git clone https://github.com/alenchavez-dev/course-management-system.git
cd course-management-system
python3 main.py
```
✅ On first run, a courses.db file will be created automatically.
You can add courses, categories, students, and scores — and they’ll all be saved between sessions.

🚀 Features
✅ OOP Structure — Uses Course and Student classes with properties, methods, and class variables

🧠 SQLite Integration — All data (courses, categories, students, and scores) is saved in courses.db for persistence between runs

✍️ Validated Input —

Semester must be two words (e.g., Fall 2025)

Course names must be two words (e.g., CIS 325)

Grading categories must be 1–5 letter acronyms (e.g., QUIZ, HW)

Student names require both first and last names

Y/N questions require valid responses

🧾 Dynamic Data Entry — Create multiple courses, categories, and students in one session

🧮 Automatic Score Recording — Enter and store scores for each grading category in the database

🧠 Clean Error Handling — Users are re-prompted until valid inputs are provided — no silent defaults

🧰 Tech Stack
Language: Python 3.x

Database: SQLite (via Python’s built-in sqlite3 module)

Concepts: Object-Oriented Programming, CLI interaction, Input Validation, SQL CRUD Operations

📂 Project Structure
bash
Copy code
course-management-system/
├── main.py          # Main program file (SQLite integrated)
├── database.py      # Handles database connection, schema creation, and CRUD operations
├── .gitignore       # Ensures the SQLite DB is not committed
├── LICENSE
└── README.md
📝 Notes
The courses.db file is auto-generated and excluded from Git tracking.

All CRUD operations are handled transparently through the database.py helper module.

You can reset the database by simply deleting the courses.db file.

🧑‍💻 Author
Alen Chavez
