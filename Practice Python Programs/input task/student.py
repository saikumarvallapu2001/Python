student_name = input("Enter the student's name: ")
age = int(input("Enter age: "))
passed_out_date = input("Enter passed out date (dd mm yyyy): ")
cgpa = float(input("Enter CGPA: "))
college_name = input("Enter college name: ")
stream = input("Enter stream: ")

programming_languages = list(map(str, input("Enter known programming languages (comma-separated): ").split()))

project_details = {
    "project": input("Enter project name: "),
    "lang": input("Enter project programming language: "),
    "role": input("Enter your role in the project: ")
}
languages_spoken = tuple(input("Enter languages spoken (space-separated): ").split())

backlog = input("Do you have any backlogs? (yes/no): ").strip().lower() == "yes"

print("\n=== Student Enrollment Details ===")
print("Student:", student_name, "| Age:", age, "| Passed Out:", passed_out_date, "| CGPA:", cgpa, "| Stream:", stream)
print("Student: %s | Age: %d | Passed Out: %s | CGPA: %.2f | Stream: %s" % (student_name, age, passed_out_date, cgpa, stream))
print(f"Student: {student_name} | Age: {age} | Passed Out: {passed_out_date} | CGPA: {cgpa:.2f} | Stream: {stream}")
print("Student: {} | Age: {} | Passed Out: {} | CGPA: {:.2f} | Stream: {}".format(student_name, age, passed_out_date, cgpa, stream))
print("Programming Languages:", ", ".join(programming_languages), sep=' ', end='\n')
print(f"Languages Spoken: {languages_spoken}")
print("\n Project Details:")
print(f"   Project Name: {project_details['project']}")
print(f"   Programming Language: {project_details['lang']}")
print(f"   Role: {project_details['role']}")

print(f"\n Backlog Status: {'Yes' if backlog else 'No'}")
