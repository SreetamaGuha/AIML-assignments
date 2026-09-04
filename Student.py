class Student:
    def __init__(self, student_id, name, department, semester, subject1, subject2, subject3):
        self.student_id = student_id
        self.name = name
        self.department = department
        self.semester = semester
        self.marks = {
            "subject1": float(subject1),
            "subject2": float(subject2),
            "subject3": float(subject3)
        }

    # Calculate total marks
    def calculate_total(self):
        return sum(self.marks.values())

    # Calculate average marks
    def calculate_average(self):
        return self.calculate_total() / 3

    # Check whether the student has passed or failed
    def get_result(self):
        for mark in self.marks.values():
            if mark < 40:
                return "FAIL"
        return "PASS"

    # Update the marks of a student
    def update_marks(self, subject1, subject2, subject3):
        self.marks["subject1"] = float(subject1)
        self.marks["subject2"] = float(subject2)
        self.marks["subject3"] = float(subject3)

    # Display student information
    def display_student(self):
        print("Student ID :", self.student_id)
        print("Name       :", self.name)
        print("Department :", self.department)
        print("Semester   :", self.semester)
        print("Subject 1  :", self.marks["subject1"])
        print("Subject 2  :", self.marks["subject2"])
        print("Subject 3  :", self.marks["subject3"])
        print("Total      :", self.calculate_total())
        print("Average    :", round(self.calculate_average(), 2))
        print("Result     :", self.get_result())
