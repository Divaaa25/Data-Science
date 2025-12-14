# Basic student information
student_name = "Rasheed Fatia"          # string
matric_number = "23/60AC389"             # string
age = 21                                 # integer
cgpa = 4.81                              # float
is_active = True                         # boolean

# Courses and grades
courses_registered = ["ELE567", "Data Science", "Statistics"]  # list
grades = {
    "Data Science": "A",
    "Statistics": "A",
    "ELE567": "B"
}  # dictionary



# Tuple for fixed department info
department_info = ("Accounting Department", "Faculty of Management Science", 2025)

# Student profiles stored as dictionaries
student_1 = {
    "name": "Rasheed Fatia",
    "matric": "23/60AC389",
    "age": 21,
    "cgpa": 4.81,
    "is_active": True,
    "courses": ["ACC 301", "FIN 345", "Statistics"],
    "outstanding_courses": 0
}

student_2 = {
    "name": "Yusuf Adeoye",
    "matric": "23/70JC093",
    "age": 22,
    "cgpa": 3.45,
    "is_active": True,
    "courses": ["ACC 301", "Statistics"],
    "outstanding_courses": 0
}

student_3 = {
    "name": "Adelaja Taiwo",
    "matric": "23/70JC002",
    "age": 20,
    "cgpa": 3.95,
    "is_active": True,
    "courses": ["FIN 345", "Statistics"],
    "outstanding_courses": 0
}

student_4 = {
    "name": "Kazeem Abimbola",
    "matric": "23/70JC003",
    "age": 23,
    "cgpa": 4.50,
    "is_active": True,
    "courses": ["FIN 345", "ACC 301"],
    "outstanding_courses": 0
}

student_5 = {
    "name": "Awe Tunde",
    "matric": "23/70JC093",
    "age": 19,
    "cgpa": 4.0,
    "is_active": True,
    "courses": ["ACC 301", "Statistics"],
    "outstanding_courses": 0
}

# List of students
students = [student_1, student_2, student_3, student_4, student_5]

# Set of unique courses
unique_courses = set()
for student in students:
    unique_courses.update(student["courses"])



def calculate_grade(score):
    if score >= 70:
        grade = "A"
    elif score >= 60:
        grade = "B"
    elif score >= 50:
        grade = "C"
    elif score >= 45:
        grade = "D"
    elif score >= 40:
        grade = "E"
    else:
        grade = "F"

    match grade:
        case "A":
            print("Excellent performance")
        case "B":
            print("Very good")
        case "C":
            print("Good effort")
        case "D":
            print("Fair")
        case "E":
            print("Needs improvement")
        case "F":
            print("Failed")

    return grade




try:
    age_input = int(input("Enter age: "))
    cgpa_input = float(input("Enter CGPA: "))

    if not (16 <= age_input <= 40):
        raise ValueError("Age must be between 16 and 40")

    if not (0.0 <= cgpa_input <= 5.0):
        raise ValueError("CGPA must be between 0.0 and 5.0")

    print("Input accepted")

except ValueError as e:
    print("Invalid input:", e)




assignment_scores = [45, 67, 89, 72, 90, 55, 60, 78, 84, 69]

top_3_scores = assignment_scores[:3]
last_5_scores = assignment_scores[-5:]
every_other_score = assignment_scores[::2]

print("Top 3:", top_3_scores)
print("Last 5:", last_5_scores)
print("Every other:", every_other_score)




set_pass = {"Rasheed", "Yusuf", "Awe", "Kazeem", "Adelaja"}
set_merit = {"Rasheed", "Kazeem", "Awe"}

passed_and_merit = set_pass & set_merit
all_students = set_pass | set_merit
passed_not_merit = set_pass - set_merit

print("Passed and Merit:", passed_and_merit)
print("All students:", all_students)
print("Passed but not merit:", passed_not_merit)



#Choice 1
def view_all_students(students):
    print("\nList of Students:")
    for index, student in enumerate(students, start=1):
        print(f"{index}. {student['name']}")


#Choice 2
def add_new_student(students):
    try:
        name = input("Enter name: ")
        matric = input("Enter matric number: ")
        age = int(input("Enter age: "))
        cgpa = float(input("Enter CGPA: "))
        is_active_input = input("Is the student active (yes/no): ").lower()
        courses_input = input("Enter courses (comma separated): ")

        is_active = True if is_active_input == "yes" else False
        courses = [course.strip() for course in courses_input.split(",")]

        new_student = {
            "name": name,
            "matric": matric,
            "age": age,
            "cgpa": cgpa,
            "is_active": is_active,
            "courses": courses,
            "outstanding_courses": 0
        }

        students.append(new_student)
        print("Student record added successfully.")

    except ValueError:
        print("Invalid input. Please enter correct data types.")


#Choice 3
def check_eligibility(student):
    if student["cgpa"] >= 2.5 and student["outstanding_courses"] == 0 and student["is_active"]:
        return True, f'{student["name"]} is eligible for graduation'
    else:
        return False, f'{student["name"]} is NOT eligible for graduation'
    
def eligibility_menu(students):
    name = input("Enter student name: ")

    for student in students:
        if student["name"].lower() == name.lower():
            status, message = check_eligibility(student)

            print("\nChecking eligibility...")
            print(f"Matric Number: {student['matric']}")
            print(f"CGPA: {student['cgpa']}")
            print(f"Outstanding Courses: {student['outstanding_courses']}")
            print(f"Active Status: {student['is_active']}")
            print("\nEligibility Result:")
            print(message)
            return

    print("Student not found.")

#Choice 4

def find_top_performer(students):
    top_student = max(students, key=lambda student: student["cgpa"])

    print("\nTop Performer:")
    print(f"Name: {top_student['name']}")
    print(f"Matric: {top_student['matric']}")
    print(f"CGPA: {top_student['cgpa']}")
    print(f"Courses: {top_student['courses']}")




while True:
    print("""
============================================
     Student Academic Performance System
============================================

1. View all students
2. Add new student
3. Check eligibility for graduation
4. Find top performer
5. Exit
""")

    choice = input("Enter your choice: ")

    match choice:
        case "1":
            view_all_students(students)

        case "2":
            add_new_student(students)

        case "3":
            eligibility_menu(students)

        case "4":
            find_top_performer(students)

        case "5":
            print("Exiting the system...")
            break

        case _:
            print("Invalid option. Please try again.")




student_scores = {
    "Rasheed": {"Python": 85, "Statistics": 78},
    "Yusuf": {"Python": 65, "Statistics": 72}
}

for name, scores in student_scores.items():
    average = sum(scores.values()) / len(scores)
    print(f"{name} average score: {average}")

    if all(score > 70 for score in scores.values()):
        print(f"{name} scored above 70 in all courses")




def identify_type(value):
    match value:
        case int():
            return "Integer detected"
        case float():
            return "Float detected"
        case list():
            return "List detected"
        case dict():
            return "Dictionary detected"
        case str():
            return "String detected"
        case _:
            return "Unknown type"



