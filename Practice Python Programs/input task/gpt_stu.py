name = input("Enter student name: ")
age = int(input("Enter age: "))
passed_out_date = input("Enter passed out date: ")
cgpa = float(input("Enter CGPA: "))
college_name = input("Enter college name: ")
stream = input("Enter stream: ")
programming_languages = list(input("Enter programming languages (space-separated): ").split())
project_name = input("Enter project name: ")
project_lang = input("Enter languages used in project (comma-separated): ")
project_role = input("Enter your role in the project: ")
languages = tuple(input("Enter languages known (comma-separated): ").split(","))
backlog = input("Do you have any backlogs? (yes/no): ").strip().lower()
student = {
    "name": name,
    "age": age,
    "passed_out_date": passed_out_date,
    "CGPA": cgpa,
    "college_name": college_name,
    "stream": stream,
    "programming_languages": programming_languages, 
    "project_details": {
        "project": project_name,
        "lang": project_lang,
        "role": project_role
    },
    "languages": languages, 
    "backlog": backlog
}

print("\nStudent Details:")
print("=" * 30)
print(f"Name: {student['name']}")
print(f"Age: {student['age']}")
print(f"Passed Out Date: {student['passed_out_date']}")
print(f"CGPA: {student['CGPA']}")
print(f"College Name: {student['college_name']}")
print(f"Stream: {student['stream']}")
print(f"Programming Languages: {', '.join(student['programming_languages'])}")
print(f"Project: {student['project_details']['project']}")
print(f"Languages Used in Project: {student['project_details']['lang']}")
print(f"Role: {student['project_details']['role']}")
print(f"Languages Known: {', '.join(student['languages'])}")
print(f"Backlog: {'Yes' if student['backlog'] == 'yes' else 'No'}")