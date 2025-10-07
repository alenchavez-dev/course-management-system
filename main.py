# 📁 main.py
# Upgraded Course Management System with SQLite integration

import database

class Category:
    def __init__(self, name, points):
        self.name = name
        self.points = points

class Course:
    def __init__(self, name, semester):
        self.name = name
        self.semester = semester
        self.categories = []
        self.students = []
        self.id = database.insert_course(name, semester)

    def enter_categories(self):
        print(f"\nEnter categories for {self.name}:")
        while True:
            cat_name = input("Category name (or blank to finish): ")
            if cat_name == "":
                break
            cat_points = float(input("Total points for this category: "))
            category = Category(cat_name, cat_points)
            self.categories.append(category)
            database.insert_category(self.id, cat_name, cat_points)

    def add_student(self, first, last):
        s = Student(first, last, self.id)
        self.students.append(s)

    def enter_scores(self):
        for s in self.students:
            print(f"\nEntering scores for {s.first} {s.last}:")
            for cat in self.categories:
                earned = float(input(f"Points earned in {cat.name} (out of {cat.points}): "))
                s.scores[cat.name] = earned
                # Get category id to insert score
                category_id = get_category_id(self.id, cat.name)
                database.insert_score(s.id, category_id, earned)

    def display_roster(self):
        print(f"\n📋 Roster for {self.name} - {self.semester}")
        for s in self.students:
            total_earned = sum(s.scores.values())
            total_possible = sum(cat.points for cat in self.categories)
            percent = (total_earned / total_possible) * 100 if total_possible > 0 else 0
            print(f"{s.first} {s.last}: {total_earned}/{total_possible} ({percent:.1f}%)")

def get_category_id(course_id, category_name):
    conn = database.get_connection()
    cur = conn.cursor()
    cur.execute("SELECT id FROM categories WHERE course_id = ? AND name = ?", (course_id, category_name))
    row = cur.fetchone()
    conn.close()
    return row[0] if row else None

class Student:
    def __init__(self, first, last, course_id):
        self.first = first
        self.last = last
        self.scores = {}
        self.id = database.insert_student(course_id, first, last)

def main():
    database.init_db()

    print("📚 Course Management System (SQL Edition)")
    course_name = input("Enter course name: ")
    semester = input("Enter semester: ")

    course = Course(course_name, semester)
    course.enter_categories()

    while True:
        print("\n[1] Add Student")
        print("[2] Enter Scores")
        print("[3] Display Roster")
        print("[4] Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            first = input("Student first name: ")
            last = input("Student last name: ")
            course.add_student(first, last)
        elif choice == "2":
            course.enter_scores()
        elif choice == "3":
            course.display_roster()
        elif choice == "4":
            break
        else:
            print("❌ Invalid choice.")

if __name__ == "__main__":
    main()

