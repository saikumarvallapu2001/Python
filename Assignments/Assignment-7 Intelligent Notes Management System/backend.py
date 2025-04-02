import json
import csv

class Person:
    def __init__(self, person_id, name, age, contact):
        self._id = person_id
        self._name = name
        self._age = age
        self._contact = contact

    def get_details(self):
        return {
            "ID": self._id,
            "Name": self._name,
            "Age": self._age,
            "Contact": self._contact
        }

class Student(Person):
    def __init__(self, student_id, name, age, contact, department):
        super().__init__(student_id, name, age, contact)
        self.department = department

class Faculty(Person):
    def __init__(self, faculty_id, name, age, contact, department, subject):
        super().__init__(faculty_id, name, age, contact)
        self.department = department
        self.subject = subject

class Department:
    def __init__(self, dept_id, name):
        self.dept_id = dept_id
        self.name = name
        self.faculty = []

    def add_faculty(self, faculty):
        if faculty not in self.faculty:
            self.faculty.append(faculty)

class University:
    def __init__(self, name):
        self.name = name
        self.students = []
        self.faculty = []
        self.departments = []

    def add_department(self, department):
        if department not in self.departments:
            self.departments.append(department)

    def register_student(self, student):
        self.students.append(student)

    def register_faculty(self, faculty):
        self.faculty.append(faculty)
        for dept in self.departments:
            if dept.name == faculty.department:
                dept.add_faculty(faculty)

    def delete_student(self, student_id):
        self.students = [s for s in self.students if s._id != student_id]

    def delete_faculty(self, faculty_id):
        self.faculty = [f for f in self.faculty if f._id != faculty_id]

    def search_student(self, student_id):
        for student in self.students:
            if student._id == student_id:
                return student
        return None

    def search_faculty(self, faculty_id):
        for faculty in self.faculty:
            if faculty._id == faculty_id:
                return faculty
        return None

    def get_statistics(self):
        return {
            "Total Students": len(self.students),
            "Total Faculty": len(self.faculty),
            "Total Departments": len(self.departments)
        }

    def export_data(self, file_format="csv"):
        data = {
            "students": [s.get_details() for s in self.students],
            "faculty": [f.get_details() for f in self.faculty],
            "departments": [{"ID": d.dept_id, "Name": d.name} for d in self.departments]
        }

        if file_format == "csv":
            with open("university_data.csv", "w", newline="") as file:
                writer = csv.DictWriter(file, fieldnames=data["students"][0].keys())
                writer.writeheader()
                writer.writerows(data["students"])
            return "Data exported to university_data.csv"

        elif file_format == "json":
            with open("university_data.json", "w") as file:
                json.dump(data, file, indent=4)
            return "Data exported to university_data.json"

        return "Invalid format"
