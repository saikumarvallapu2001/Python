from tabulate import tabulate

# Input details
student_name = input("Enter the student's name: ")
age = int(input("Enter age: "))
passed_out_date = input("Enter passed out date (dd mm yyyy): ")
cgpa = float(input("Enter CGPA: "))
college_name = input("Enter college name: ")
stream = input("Enter stream: ")

programming_languages = list(map(str.strip, input("Enter known programming languages (comma-separated): ").split(",")))

project_details = {
    "project": input("Enter project name: "),
    "lang": input("Enter project programming language: "),
    "role": input("Enter your role in the project: ")
}
languages_spoken = tuple(input("Enter languages spoken (space-separated): ").split())

backlog = input("Do you have any backlogs? (yes/no): ").strip().lower() == "yes"

# Formatting data into tables
student_data = [
    ["Student Name", student_name],
    ["Age", age],
    ["Passed Out Date", passed_out_date],
    ["CGPA", f"{cgpa:.2f}"],
    ["Stream", stream],
    ["College", college_name],
    ["Backlog", "Yes" if backlog else "No"]
]

programming_table = [[lang] for lang in programming_languages]
languages_table = [[lang] for lang in languages_spoken]

project_table = [
    ["Project Name", project_details["project"]],
    ["Programming Language", project_details["lang"]],
    ["Role", project_details["role"]]
]

# Display tables
print("\n=== Student Enrollment Details ===")
print(tabulate(student_data, tablefmt="grid"))

print("\n=== Programming Languages Known ===")
print(tabulate(programming_table, headers=["Languages"], tablefmt="grid"))

print("\n=== Languages Spoken ===")
print(tabulate(languages_table, headers=["Languages"], tablefmt="grid"))

print("\n=== Project Details ===")
print(tabulate(project_table, tablefmt="grid"))
