# ============================================================
# Program: Course Management System
# Author: Alen Chavez
# Description:
#   This program simulates a simple course management system.
#   It allows the user to create multiple courses, define grading
#   categories with up-to-5-letter acronyms, validate semester
#   and course name inputs (2 words), enroll students with proper
#   name validation, enter scores, and display course information
#   for a given semester.
#   It demonstrates OOP principles in Python through Course and
#   Student classes, and provides interactive input via the console.
# ============================================================

class Course:
    semester = ""  # Shared semester for all courses

    def __init__(self, name: str, categories: dict = None):
        """
        Initialize a new course with its name and grading categories.
        """
        self.section = 0
        self.name = name
        self.student_count = 0
        self.class_roster = []
        if categories is None:
            self.categories = {}
            self.enter_categories()
        else:
            self.categories = categories

    def enter_categories(self):
        """
        Prompt the user to enter grading categories (up to 5-letter acronyms)
        and their point values, with input validation.
        """
        print(f'Enter grading categories for {self.name}')
        while True:
            # ✅ Force 1–5 letter acronym (alphabetic only)
            while True:
                category = input('Enter a grading category (1–5 letter acronym, e.g., QUIZ): ').strip().upper()
                if 1 <= len(category) <= 5 and category.isalpha():
                    break
                print("❌ Invalid category. Please enter 1 to 5 alphabetic characters.")

            points = ask_int(f'Enter the points that {category} is worth: ')
            self.categories[category] = points

            if not ask_yes_no('Do you have more categories to enter (Y/N): '):
                break

    def enroll_students(self, number):
        """
        Enroll a given number of students in this course.
        """
        self.student_count += number
        for _ in range(number):
            temp_student = Student(self.categories)
            temp_student.fullname = input('Enter student first and last name (e.g., Alen Chavez): ')
            temp_student.enter_scores()
            self.class_roster.append(temp_student)

    def __str__(self):
        """
        Return a formatted string of course information, including each student’s scores.
        """
        message = f'Course {self.section} – {self.name} has {self.student_count} students:\n'
        for student in self.class_roster:
            message += f'{student} – '
            for category in self.categories:
                message += f'{category}: {student.scores[category]} / {self.categories[category]}, '
            message = message.rstrip(', ')
            message += '\n'
        return message

    @classmethod
    def change_semester(cls, semester: str):
        """
        Change the semester for all courses.
        """
        cls.semester = semester


class Student:
    def __init__(self, categories: dict):
        """
        Initialize a student with empty name and category scores.
        """
        self.first = ""
        self.last = ""
        self.scores = {category: 0 for category in categories}

    @property
    def fullname(self):
        return f'{self.last}, {self.first}'

    @fullname.setter
    def fullname(self, name):
        """
        Parse and validate full name input. Keeps asking until a valid
        first and last name are entered.
        """
        while True:
            parts = name.strip().split()
            if len(parts) >= 2:
                self.first = parts[0]
                self.last = " ".join(parts[1:])
                break
            print("❌ Please enter both a first and last name (e.g., Alen Chavez).")
            name = input("Enter student first and last name (e.g., Alen Chavez): ")

    def enter_scores(self):
        """
        Prompt for and store the student's scores for each category.
        """
        for category in self.scores:
            score = ask_int(f'Enter earned points for {category}: ')
            self.scores[category] = score

    def __str__(self):
        return self.fullname


# ============================================================
# Helper Functions
# ============================================================

def ask_int(prompt: str) -> int:
    """
    Repeatedly prompt the user for an integer until valid input is received.
    """
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("❌ Please enter a valid whole number.")


def ask_yes_no(prompt: str) -> bool:
    """
    Prompt the user with a yes/no question and return True for 'Y', False for 'N'.
    Keeps asking until valid input is received.
    """
    while True:
        response = input(prompt).strip().upper()
        if response in ('Y', 'N'):
            return response == 'Y'
        print("❌ Invalid input. Please enter 'Y' or 'N'.")


def ask_two_word_input(prompt: str) -> str:
    """
    Prompt the user for a two-word input (e.g., 'Fall 2025' or 'CIS 325').
    Keeps asking until the input contains at least two words.
    """
    while True:
        value = input(prompt).strip()
        parts = value.split()
        if len(parts) >= 2:
            return value
        print("❌ Please enter at least two words (e.g., Fall 2025 or CIS 325).")


# ============================================================
# Main Program Logic
# ============================================================

if __name__ == "__main__":
    print("Welcome to the Course Management System")
    # ✅ Force 2-word semester (e.g., Fall 2025)
    Course.change_semester(ask_two_word_input("Enter the semester for the courses (e.g., Fall 2025): "))

    courses = []
    course_number = 0

    # Create courses
    while True:
        # ✅ Force 2-word course name (e.g., CIS 325)
        course_name = ask_two_word_input("Enter the course name (e.g., CIS 325): ")
        new_course = Course(course_name)
        new_course.section = course_number
        course_number += 1
        courses.append(new_course)

        if not ask_yes_no("Do you want to enter another course? (Y/N): "):
            break

    # Enroll students in each course
    for course in courses:
        print(f'\nAdd students to {course.name} course')
        num_students = ask_int('How many students do you want to enroll? ')
        if num_students > 0:
            course.enroll_students(num_students)

    # Display summary
    print(f'\nCourse Information for {Course.semester}')
    for course in courses:
        print(course)
