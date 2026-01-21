# Student Course Registration System (SCRS)
# Fixed Login Credentials for SEN Assignment

USERNAME = "Nelson"
PASSWORD = "1234"

courses = ["CSC101", "CSC102", "CSC201", "CSC202"]
registered_courses = []


def login_student():
    username = input("Enter username: ")
    password = input("Enter password: ")

    if username == USERNAME and password == PASSWORD:
        print("Login successful.")
        student_menu()
    else:
        print("Invalid username or password.")


def view_courses():
    print("\nAvailable Courses:")
    for course in courses:
        print(course)


def register_course():
    view_courses()
    course = input("Enter course code to register: ")

    if course in courses:
        if course in registered_courses:
            print("Course already registered.")
        else:
            registered_courses.append(course)
            print("Course registered successfully.")
    else:
        print("Invalid course code.")


def view_registered_courses():
    print("\nRegistered Courses:")
    if registered_courses:
        for course in registered_courses:
            print(course)
    else:
        print("No courses registered.")


def student_menu():
    while True:
        print("\n1. View Courses")
        print("2. Register Course")
        print("3. View Registered Courses")
        print("4. Logout")

        choice = input("Choose an option: ")

        if choice == "1":
            view_courses()
        elif choice == "2":
            register_course()
        elif choice == "3":
            view_registered_courses()
        elif choice == "4":
            print("Logging out...")
            break
        else:
            print("Invalid choice.")


def main_menu():
    while True:
        print("\nSTUDENT COURSE REGISTRATION SYSTEM")
        print("1. Login")
        print("2. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            login_student()
        elif choice == "2":
            print("Exiting system...")
            break
        else:
            print("Invalid choice.")


main_menu()
