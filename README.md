# 🧠 Course Management System

A fully interactive, object-oriented Python console application that simulates a simple course management system.  
This program allows users to:

- Create courses with validated **two-word names** (e.g., “CIS 325”)  
- Define grading categories using **1–5 letter acronyms**  
- Input and validate **semester names** (e.g., “Fall 2025”)  
- Enroll students with proper **first + last name validation**  
- Enter scores for multiple grading categories  
- Display a complete course roster with scores for each student

It’s designed to demonstrate strong **Python fundamentals**, **object-oriented programming**, and **robust input validation**, making it an excellent portfolio piece for IT/programming roles.

---

## 🚀 Features

- ✅ **OOP Structure** — Uses `Course` and `Student` classes with properties, methods, and class variables  
- ✍️ **Validated Input** —  
  - Semester must be two words (e.g., `Fall 2025`)  
  - Course names must be two words (e.g., `CIS 325`)  
  - Grading categories must be 1–5 letter acronyms (e.g., `QUIZ`, `HW`)  
  - Student names require both first and last names  
  - Y/N questions require valid responses  
- 🧾 **Dynamic Data Entry** — Create multiple courses, categories, and students in one session  
- 🧮 **Automatic Score Recording** — Enter and display scores for each grading category  
- 🧠 **Clean Error Handling** — Users are re-prompted until valid inputs are provided — no silent defaults

---

## 🧰 Tech Stack

- **Language:** Python 3.x  
- **Concepts:** Object-Oriented Programming, CLI interaction, Input Validation

---

## 📂 Project Structure

```bash
course-management-system/
├── course_management.py   # Main program file
└── README.md              # Project documentation
