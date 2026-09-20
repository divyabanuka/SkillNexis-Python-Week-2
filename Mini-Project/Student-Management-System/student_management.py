# SkillNexis Python Programming
# Week 2 - Mini Project
# Student Management System

import csv
import os

FILE_NAME = "students.csv"


def initialize_file():
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Roll Number", "Name", "Marks"])


def add_student():
    roll = input("Enter roll number: ")
    name = input("Enter student name: ")
    marks = input("Enter marks: ")

    with open(FILE_NAME, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([roll, name, marks])

    print("Student added successfully!")


def view_students():
    with open(FILE_NAME, "r") as file:
        reader = csv.reader(file)

        print("\n========== STUDENTS ==========")

        for row in reader:
            print(" | ".join(row))

        print("==============================")


def search_student():
    roll = input("Enter roll number to search: ")

    found = False

    with open(FILE_NAME, "r") as file:
        reader = csv.DictReader(file)

        for student in reader:
            if student["Roll Number"] == roll:
                print("\nStudent Found!")
                print("Roll Number:", student["Roll Number"])
                print("Name:", student["Name"])
                print("Marks:", student["Marks"])
                found = True
                break

    if not found:
        print("Student not found.")


def delete_student():
    roll = input("Enter roll number to delete: ")

    students = []
    found = False

    with open(FILE_NAME, "r") as file:
        reader = csv.DictReader(file)

        for student in reader:
            if student["Roll Number"] == roll:
                found = True
            else:
                students.append(student)

    if found:
        with open(FILE_NAME, "w", newline="") as file:
            fieldnames = ["Roll Number", "Name", "Marks"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)

            writer.writeheader()
            writer.writerows(students)

        print("Student deleted successfully!")
    else:
        print("Student not found.")


def main():
    initialize_file()

    while True:
        print("\n================================")
        print("     STUDENT MANAGEMENT SYSTEM")
        print("================================")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Delete Student")
        print("5. Exit")
        print("================================")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_student()

        elif choice == "2":
            view_students()

        elif choice == "3":
            search_student()

        elif choice == "4":
            delete_student()

        elif choice == "5":
            print("Thank you!")
            break

        else:
            print("Invalid choice. Please try again.")


main()