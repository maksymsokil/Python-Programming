"""
Main program for the Student Record Manager project.

This file imports custom modules to:
1. Calculate averages and letter grades
2. Save student reports to a file

It demonstrates two import styles:
- import module_name
- from module_name import function
"""

import grade_utils
from file_utils import save_report, display_report
from datetime import datetime


def get_student_data():
    """
    Collect student names and grades from the user.
    Returns a list of dictionaries.
    """
    students = []

    print("Student Record Manager")
    print("----------------------")

    while True:
        name = input("Enter student name (or type 'done' to finish): ").strip()

        if name.lower() == "done":
            break

        try:
            grade1 = float(input("Enter first grade: "))
            grade2 = float(input("Enter second grade: "))
            grade3 = float(input("Enter third grade: "))
        except ValueError:
            print("Invalid input. Please enter numeric grades only.\n")
            continue

        average = grade_utils.calculate_average([grade1, grade2, grade3])
        letter = grade_utils.get_letter_grade(average)
        passed = grade_utils.did_pass(average)

        students.append({
            "name": name,
            "grades": [grade1, grade2, grade3],
            "average": average,
            "letter": letter,
            "passed": passed
        })

        print()

    return students


def build_report(students):
    """
    Build a formatted report string for all students.
    """
    report_lines = []
    report_lines.append("Student Record Report")
    report_lines.append(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    report_lines.append("-" * 50)

    if not students:
        report_lines.append("No student records were entered.")
        return "\n".join(report_lines)

    for student in students:
        line = (
            f"Name: {student['name']} | "
            f"Grades: {student['grades']} | "
            f"Average: {student['average']:.2f} | "
            f"Letter Grade: {student['letter']} | "
            f"Passed: {'Yes' if student['passed'] else 'No'}"
        )
        report_lines.append(line)

    class_average = grade_utils.calculate_class_average(students)
    report_lines.append("-" * 50)
    report_lines.append(f"Class Average: {class_average:.2f}")

    return "\n".join(report_lines)


def main():
    """
    Main function that runs the program.
    """
    students = get_student_data()
    report = build_report(students)

    print("\nFinal Report")
    print("------------")
    display_report(report)

    save_report("student_report.txt", report)
    print("\nReport saved to student_report.txt")


if __name__ == "__main__":
    main()