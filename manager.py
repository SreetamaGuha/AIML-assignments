from student import Student
import file_handler

class StudentManager:
    def __init__(self):
        self.students = []

    # Add a new Student object
    def add_student(self, student):
        if self.search_student(student.student_id) is not None:
            print("Student ID already exists.")
            return False
        self.students.append(student)
        print("Student added successfully.")
        return True

    # Remove a student using Student ID
    def remove_student(self, student_id):
        student = self.search_student(student_id)
        if student is not None:
            self.students.remove(student)
            print("Student removed successfully.")
            return True
        print("Student not found.")
        return False

    # Search for a student using Student ID
    def search_student(self, student_id):
        for student in self.students:
            if str(student.student_id) == str(student_id):
                return student
        return None

    # Display all students
    def display_all_students(self):
        if not self.students:
            print("No student records available.")
            return

        for student in self.students:
            student.display_student()

    # Save students to a file
    def save_to_file(self, filename, file_format):
        file_handler.save_students(
            self.students,
            filename,
            file_format
        )

    # Load students from a file
    def load_from_file(self, filename, file_format):
        self.students = file_handler.load_students(
            filename,
            file_format
        )
