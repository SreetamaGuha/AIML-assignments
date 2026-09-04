import sys

from student import Student
from manager import StudentManager


# Create StudentManager object
manager = StudentManager()

# Add Student

def addStudent():

    if len(sys.argv) < 9:

        print("\nPlease provide all student details.")
        print("Example:")
        print("python main.py add 106 Sreetama ComputerScience 1 85 78 91")
        return

    studentId = sys.argv[2]
    name = sys.argv[3]
    department = sys.argv[4]
    semester = sys.argv[5]
    mark1 = sys.argv[6]
    mark2 = sys.argv[7]
    mark3 = sys.argv[8]

    student = Student(
        studentId,
        name,
        department,
        semester,
        mark1,
        mark2,
        mark3
    )

    manager.add_student(student)


# Display all students
def displayAllStudents():

    if len(sys.argv) < 3:

        print("Please provide the file name and format.")
        print("Example: python main.py display data/students.csv csv")
        return

    filename = sys.argv[2]
    file_format = sys.argv[3]

    manager.load_from_file(filename, file_format)
    manager.display_all_students()

# Search Student by ID

def searchStudentById(studentId):

    if len(sys.argv) < 5:

        print("Please provide the file name and format.")
        print("Example: python main.py search 101 data/students.csv csv")
        return

    filename = sys.argv[3]
    file_format = sys.argv[4]
    manager.load_from_file(filename, file_format)
    student = manager.search_student(studentId)

    if student is not None:
        student.display_student()

    else:
        print("Student not found.")

# Save Data

def save_json():
    if len(sys.argv) < 4:
        print("Please provide input file and output file.")
        return

    input_file = sys.argv[2]
    output_file = sys.argv[3]

    manager.load_from_file(input_file, "csv")
    manager.save_to_file(output_file, "json")
    print("Data saved to JSON successfully.")

def save_txt():
    if len(sys.argv) < 4:
        print("Please provide input file and output file.")
        return

    input_file = sys.argv[2]
    output_file = sys.argv[3]

    manager.load_from_file(input_file, "csv")
    manager.save_to_file(output_file, "txt")
    print("Data saved to TXT successfully.")


def save_csv():
    if len(sys.argv) < 4:
        print("Please provide input file and output file.")
        return

    input_file = sys.argv[2]
    output_file = sys.argv[3]

    manager.load_from_file(input_file, "csv")
    manager.save_to_file(output_file, "csv")
    print("Data saved to CSV successfully.")

# Read Data
def read_json():
    if len(sys.argv) < 3:
        print("Please provide the JSON file name.")
        return

    filename = sys.argv[2]
    manager.load_from_file(filename, "json")
    manager.display_all_students()

def read_txt():
    if len(sys.argv) < 3:
        print("Please provide the TXT file name.")
        return

    filename = sys.argv[2]
    manager.load_from_file(filename, "txt")
    manager.display_all_students()


def read_csv():
    if len(sys.argv) < 3:
        print("Please provide the CSV file name.")
        return
    filename = sys.argv[2]
    manager.load_from_file(filename, "csv")
    manager.display_all_students()

# Main Function

def main():
    if len(sys.argv) < 2:
        print("\n----- Student Management System -----")
        print("1. Add Student")
        print("2. Display All Students")
        print("3. Search Student by ID")
        print("4. Save Data to JSON")
        print("5. Save Data to TXT")
        print("6. Save Data to CSV")
        print("7. Read Data from JSON")
        print("8. Read Data from TXT")
        print("9. Read Data from CSV")
        print("0. Exit")

        sys.exit()
    command = sys.argv[1]

    # To add a student
    if command == "add":
        addStudent()


    # To display all students
    elif command == "display":
        displayAllStudents()


    # To search student by ID
    elif command == "search":
        if len(sys.argv) < 3:

            print("Please provide a student ID to search.")
            sys.exit()

        studentId = sys.argv[2]
        searchStudentById(studentId)


    # To save data
    elif command == "save":
        if len(sys.argv) < 3:
            print("Please provide a file format to save (json/txt/csv).")
            sys.exit()

        else:
            file_format = sys.argv[2].lower()
            if file_format == "json":
                save_json()

            elif file_format == "txt":
                save_txt()

            elif file_format == "csv":
                save_csv()

            else:

                print("Invalid file format.")
                print("Please choose from json, txt, or csv.")


    # To read data
    elif command == "read":
        if len(sys.argv) < 3:
            print("Please provide a file format to read (json/txt/csv).")
            sys.exit()

        else:
            file_format = sys.argv[2].lower()
            if file_format == "json":
                read_json()

            elif file_format == "txt":
                read_txt()

            elif file_format == "csv":
                read_csv()

            else:

                print("Invalid file format.")
                print("Please choose from json, txt, or csv.")


    else:

        print("Invalid command.")
        print("Please choose from add, display, search, save, or read.")


# Program starts here
if __name__ == "__main__":
    main()
