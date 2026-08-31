import sys
import csv
import json


# Student class to store student information
class Student:
    def __init__(self, studentId, name, dept, sem,
                 mark1, mark2, mark3):

        self.studentId = studentId
        self.name = name
        self.dept = dept
        self.sem = sem
        self.marks = [mark1, mark2, mark3]

    # To calculate the total marks
    def totalMarks(self):
        return sum(self.marks)

    # To calculate the average marks
    def averageMarks(self):
        return sum(self.marks) / len(self.marks)

    # To check pass or fail
    def result(self):
        if all(mark >= 40 for mark in self.marks):
            return "Pass"
        else:
            return "Fail"

    # To search student by ID
    def searchStudentById(self, studentId):
        if self.studentId == studentId:
            return self

        return None

    # To display student information
    def display(self):

        print("\n----- Student Information -----")
        print("Student ID :", self.studentId)
        print("Name       :", self.name)
        print("Department :", self.dept)
        print("Semester   :", self.sem)
        print("Subject 1  :", self.marks[0])
        print("Subject 2  :", self.marks[1])
        print("Subject 3  :", self.marks[2])
        print("Total Marks:", self.totalMarks())
        print("Average    :", round(self.averageMarks(), 2))
        print("Result     :", self.result())


# Create a list to store student objects
students = []


# To add a new student
def addStudent():
    #Load existing students first
    read_json()
    studentId = input("Enter Student ID: ")
    name = input("Enter Student Name: ")
    dept = input("Enter Department: ")
    sem = input("Enter Semester: ")
    mark1 = float(input("Enter Marks for Subject 1: "))
    mark2 = float(input("Enter Marks for Subject 2: "))
    mark3 = float(input("Enter Marks for Subject 3: "))
    student = Student( studentId, name, dept, sem, mark1, mark2, mark3 )
    students.append(student)
    #Save ALL students
    save_json()
    save_txt()
    save_csv()
    print("\nStudent added successfully!")


# To display all students
def displayAllStudents():
    # Load saved students
    read_json()
    if not students:
        print("\nNo students found.")
        return

    for student in students:
        student.display()




# To create a dictionary of student data
def studentToDict(student):

    return {
        "studentId": student.studentId,
        "name": student.name,
        "dept": student.dept,
        "sem": student.sem,
        "marks": student.marks
    }


# To save student data to JSON
def save_json():
    with open("students.json", "w") as file:
        json.dump([studentToDict(student) for student in students], file, indent=4)
    print("Data saved to students.json")


# To save student data to TXT
def save_txt():
    with open("students.txt", "w") as file:
        for student in students:
            file.write(f"Student ID: {student.studentId}\n")
            file.write(f"Name: {student.name}\n")
            file.write(f"Department: {student.dept}\n")
            file.write(f"Semester: {student.sem}\n")
            file.write(f"Subject 1: {student.marks[0]}\n")
            file.write(f"Subject 2: {student.marks[1]}\n")
            file.write(f"Subject 3: {student.marks[2]}\n")
            file.write(f"Total Marks: {student.totalMarks()}\n")
            file.write(f"Average Marks: {round(student.averageMarks(), 2)}\n")
            file.write(f"Result: {student.result()}\n")
            file.write("\n")

    print("Data saved to students.txt")


# To save student data to CSV
def save_csv():

    with open("students.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Student ID", "Name", "Department", "Semester", "Subject 1", "Subject 2", "Subject 3"])

        for student in students:
            writer.writerow([student.studentId, student.name, student.dept, student.sem, student.marks[0], student.marks[1], student.marks[2]])
    print("Data saved to students.csv")


# To read student data from JSON
def read_json():
    try:
        with open("students.json", "r") as file:
            data = json.load(file)
            students.clear()
            for student_data in data:
                student = Student(student_data["studentId"], student_data["name"], student_data["dept"], student_data["sem"], *student_data["marks"])
                students.append(student)
        print("Data loaded from students.json")

    except FileNotFoundError:
        print("students.json file not found.")


# To read student data from TXT
def read_txt():
    try:
        with open("students.txt", "r") as file:
            students.clear()
            lines = []

            for line in file:
                line = line.strip()
                if line:
                    lines.append(line)

            # Each student has 10 lines
            for i in range(0, len(lines), 10):
                studentId = lines[i].split(": ", 1)[1]
                name = lines[i + 1].split(": ", 1)[1]
                dept = lines[i + 2].split(": ", 1)[1]
                sem = lines[i + 3].split(": ", 1)[1]

                mark1 = float(lines[i + 4].split(": ", 1)[1])
                mark2 = float(lines[i + 5].split(": ", 1)[1])
                mark3 = float(lines[i + 6].split(": ", 1)[1])

                student = Student(studentId, name, dept, sem, mark1, mark2, mark3)
                students.append(student)
        print("Data loaded from students.txt")

    except FileNotFoundError:
        print("students.txt file not found.")


# To read student data from CSV
def read_csv():
    try:
        with open("students.csv", "r") as file:
            students.clear()
            reader = csv.reader(file)

            # Skip header
            next(reader)
            for row in reader:
                studentId = row[0]
                name = row[1]
                dept = row[2]
                sem = row[3]

                mark1 = float(row[4])
                mark2 = float(row[5])
                mark3 = float(row[6])
                student = Student(studentId, name, dept, sem, mark1, mark2, mark3)
                students.append(student)
        print("Data loaded from students.csv")

    except FileNotFoundError:
        print("students.csv file not found.")


def main():
    # Display this menu when no commands are there
    if len(sys.argv) == 1:
        print("\nMenu:")
        print("1. add")
        print("2. display")
        print("3. search <studentId>")
        print("4. save <json/txt/csv>")
        print("5. read <json/txt/csv>")
        print("6. exit")

        return

    # To take command line agrument
    command = sys.argv[1].lower()

    #To ad students
    if command == "add":
        addStudent()
    
    #To display the informations
    elif command == "display":
        # Load existing data first
        read_json()

        displayAllStudents()

    #To search students by id 
    elif command == "search":

        if len(sys.argv) < 3:
            print("Please provide a student ID.")
            print("Example: python student.py search 101")

        else:

            read_json()
            studentId = sys.argv[2]
            searchStudentById(studentId)
            
    #Exit
    elif command == "exit":
        print("Program terminated.")

    #From ivalid command 
    else:

        print("Invalid command.")
        print("\nAvailable commands:")
        print("add")
        print("display")
        print("search <studentId>")
        print("exit")

# Run main function
if __name__ == "__main__":
    main()
