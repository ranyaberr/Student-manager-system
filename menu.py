from db import conn
from student_service import add_student, delete_student, search_student, update_student, view_students

#MENU

def menu():
    while True:
        print("\n======= Student Management System =======")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Delete Student")
        print("5. Update Student")
        print("6. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            delete_student()
        elif choice == "5":
            update_student()
        elif choice == "6":
            print("Have a good day!")
            break
        else:
            print("Invalid option!")

