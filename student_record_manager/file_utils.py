"""
file_utils.py

This module handles file operations and report display
for the Student Record Manager project.
"""


def save_report(filename, report_text):
    """
    Save the report text to a file.
    """
    with open(filename, "w") as file:
        file.write(report_text)


def display_report(report_text):
    """
    Print the report to the screen.
    """
    print(report_text)