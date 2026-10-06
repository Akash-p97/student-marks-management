# Student Marks Management
# Python Project

students = [
    {"name": "Akash", "marks": 95},
    {"name": "Rahul", "marks": 80},
    {"name": "Amit", "marks": 70},
    {"name": "Priya", "marks": 85},
    {"name": "Neha", "marks": 90}
]


def display_students(students):
    print("Student Marks:")
    for student in students:
        print(student["name"], "-", student["marks"])


def calculate_results(students):
    marks = [student["marks"] for student in students]

    average = sum(marks) / len(marks)
    highest = max(marks)
    lowest = min(marks)

    passed = 0
    failed = 0

    for student in students:
        if student["marks"] >= 40:
            passed += 1
        else:
            failed += 1

    print("\nResults")
    print("Average Marks:", average)
    print("Highest Marks:", highest)
    print("Lowest Marks:", lowest)
    print("Passed Students:", passed)
    print("Failed Students:", failed)


display_students(students)
calculate_results(students)
