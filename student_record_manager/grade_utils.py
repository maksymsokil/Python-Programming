"""
grade_utils.py

This module handles all grade-related calculations for the
Student Record Manager project.
"""


def calculate_average(grades):
    """
    Return the average of a list of grades.
    """
    return sum(grades) / len(grades)


def get_letter_grade(average):
    """
    Convert a numeric average into a letter grade.
    """
    if average >= 90:
        return "A"
    elif average >= 80:
        return "B"
    elif average >= 70:
        return "C"
    elif average >= 60:
        return "D"
    else:
        return "F"


def did_pass(average):
    """
    Return True if the student passed, otherwise False.
    """
    return average >= 60


def calculate_class_average(students):
    """
    Return the average of all student averages.
    """
    if not students:
        return 0
    total = sum(student["average"] for student in students)
    return total / len(students)