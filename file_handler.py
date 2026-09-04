import csv
import json

from student import Student

#Functions for text file
def load_from_txt(filename):
    students = []

    with open(filename, "r") as file:
        lines = file.readlines()

        for line in lines:
            line = line.strip()

            if not line:
                continue

            values = line.split(",")
            student = Student(
                values[0].strip(),
                values[1].strip(),
                values[2].strip(),
                values[3].strip(),
                values[4].strip(),
                values[5].strip(),
                values[6].strip()
            )
            students.append(student)
    return students


def save_to_txt(students, filename):
    with open(filename, "w") as file:

        for student in students:
            line = (
                f"{student.student_id}, "
                f"{student.name}, "
                f"{student.department}, "
                f"{student.semester}, "
                f"{student.marks['subject1']}, "
                f"{student.marks['subject2']}, "
                f"{student.marks['subject3']}\n"
            )
            file.write(line)

#Functions for csv files 
def load_from_csv(filename):
    students = []

    with open(filename, "r", newline="") as file:
        reader = csv.reader(file)

        # Skip the header row
        next(reader, None)
        for row in reader:
            student = Student(
                row[0],
                row[1],
                row[2],
                row[3],
                row[4],
                row[5],
                row[6]
            )
            students.append(student)
    return students


def save_to_csv(students, filename):
    with open(filename, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([
            "Student_ID",
            "Name",
            "Department",
            "Semester",
            "Subject1",
            "Subject2",
            "Subject3"
        ])
        for student in students:
            writer.writerow([
                student.student_id,
                student.name,
                student.department,
                student.semester,
                student.marks["subject1"],
                student.marks["subject2"],
                student.marks["subject3"]
            ])

#Functions for JSON files

def load_from_json(filename):
    students = []

    with open(filename, "r") as file:
        data = json.load(file)
        for item in data:
            student = Student(item["student_id"], item["name"], item["department"], item["semester"], item["marks"]["subject1"], item["marks"]["subject2"], item["marks"]["subject3"])
            students.append(student)
    return students


def save_to_json(students, filename):
    data = []
    for student in students:
        student_data = {
            "student_id": student.student_id,
            "name": student.name,
            "department": student.department,
            "semester": student.semester,
            "marks": {
                "subject1": student.marks["subject1"],
                "subject2": student.marks["subject2"],
                "subject3": student.marks["subject3"]
            }
        }

        data.append(student_data)
    with open(filename, "w") as file:
        json.dump(data, file, indent=4)

#Save functions
def save_students(students, filename, file_format):
    if file_format == "txt":
        save_to_txt(students, filename)

    elif file_format == "csv":
        save_to_csv(students, filename)

    elif file_format == "json":
        save_to_json(students, filename)

    else:
        raise ValueError("Unsupported file format.")


#Functions to load
def load_students(filename, file_format):
    if file_format == "txt":
        return load_from_txt(filename)

    elif file_format == "csv":
        return load_from_csv(filename)

    elif file_format == "json":
        return load_from_json(filename)

    else:
        raise ValueError("Unsupported file format.")
