import sys

# Data storage
students = {}
subjects = {}
grades = {}  # {student_Name: {subject_name: grade}}

def pause():
    input("\nPress Enter to continue...")

#studnets
def add_student():
#auto generate from 001 to 900 hehe
    if students:
        next_Name = max(int(sName) for sName in students.keys()) + 1
    else:
        next_Name = 1
    student_Name = f"{next_Name:03d}" # ion knwow internet tells me to to this for 3 zeroes


    name = input("Enter student name: ")
    students[student_Name] = name
    print(f"\nStudent added successfully! Assigned Name: {student_Name}!")


def edit_student():
    student_Name = input("Enter student Name to edit: ")
    if student_Name not in students:
        print("\nStudent not found!")
        return
    new_name = input("Enter new name: ")
    students[student_Name] = new_name
    print("\nStudent updated!")


def delete_student():
    student_Name = input("Enter student Name to delete: ")
    if student_Name not in students:
        print("\nStudent not found!")
        return
    students.pop(student_Name)
    grades.pop(student_Name, None)
    print("\nStudent deleted!")


def view_students():
    if not students:
        print("\nNo students available.")
        return
    print("\n--- STUDENTS LIST ---")
    for sName, name in students.items():
        print(f"Name: {sName} | Name: {name}")

#subjeckerz
def add_subject():
    subject_name = input("Enter subject Name: ")
    if subject_name in subjects:
        print("\nSubject already exists!")
        return
    subjects[subject_name] = subject_name
    print("\nSubject added!")



def edit_subject():
    subject_name = input("Enter subject Name to edit: ")
    if subject_name not in subjects:
        print("\nSubject not found!")
        return
    new_name = input("Enter new subject name: ")
    subjects[subject_name] = new_name
    print("\nSubject updated!")


def delete_subject():
    subject_name = input("Enter subject Name to delete: ")
    if subject_name not in subjects:
        print("\nSubject not found!")
        return
    subjects.pop(subject_name) #pop is remove ong dont forget to explain to felixz
    for sName in grades:
        grades[sName].pop(subject_name, None)
    print("\nSubject deleted!")


def view_subjects():
    if not subjects:
        print("No subjects available.")
        return
    print("\n--- SUBJECTS LIST ---")
    for name in subjects:
        print(f"{name}")

#GRades
def pick_student():
    if not students:
        print("\nNo students available!")
        return None
    view_students()
    return input("Enter student Name: ")


def pick_subject():
    if not subjects:
        print("\nNo subjects available!")
        return None
    view_subjects()
    return input("Enter subject Name: ")


def add_grade():
    sName = pick_student()
    if not sName or sName not in students:
        print("\nInvalid student!")
        return
    sub = pick_subject()
    if not sub or sub not in subjects:
        print("\nInvalid subject!")
        return
    grade = input("Enter grade: ")
    grades.setdefault(sName, {})[sub] = grade
    print("\nGrade added!")


def edit_grade():
    sName = pick_student()
    if not sName or sName not in grades:
        print("\nNo grades for this student.")
        return
    sub = pick_subject()
    if not sub or sub not in grades[sName]:
        print("\nNo grade for this subject.")
        return
    grade = input("Enter new grade: ")
    grades[sName][sub] = grade
    print("\nGrade updated!")


def delete_grade():
    sName = pick_student()
    if not sName or sName not in grades:
        print("\nNo grades for this student.")
        return
    sub = pick_subject()
    if not sub or sub not in grades[sName]:
        print("\nGrade not found.")
        return
    grades[sName].pop(sub)
    print("\nGrade deleted!")


def view_student_grades():
    sName = pick_student()
    if not sName or sName not in students:
        print("\nInvalid student.")
        return
    print(f"\nGrades for {students[sName]}:")
    if sName not in grades or not grades[sName]:
        print("\nNo grades available.")
        return
    for sub, g in grades[sName].items():
        print(f"{subjects.get(sub, 'Unknown')} ({sub}): {g}")

#Main MENU 
def menu():
    while True:
        print("\n===== GRADE CHECKER SYSTEM =====")
        print("1. Manage Students")
        print("2. Manage Subjects")
        print("3. Input Grades")
        print("4. View Grades")
        print("5. Exit")
        choice = input("Select an option: ")

        if choice == "1":
            student_menu()
        elif choice == "2":
            subject_menu()
        elif choice == "3":
            grade_menu()
        elif choice == "4":
            view_student_grades()
            pause()
        elif choice == "5":
            print("\nExiting system...")
            sys.exit()
        else:
            print("Invalid choice!")


def student_menu():
    while True:
        print("\n--- MANAGE STUDENTS ---")
        print("1. Add")
        print("2. Edit")
        print("3. Delete")
        print("4. View")
        print("0. Back")
        choice = input("Select: ")

        if choice == "1": add_student() 
        elif choice == "2": edit_student()
        elif choice == "3": delete_student()
        elif choice == "4": view_students()
        elif choice == "0": break
        else: print("\nInvalid Choice!")
        pause()


def subject_menu():
    while True:
        print("\n--- MANAGE SUBJECTS ---")
        print("1. Add")
        print("2. Edit")
        print("3. Delete")
        print("4. View")
        print("0. Back")
        choice = input("Select: ")

        if choice == "1": add_subject()
        elif choice == "2": edit_subject()
        elif choice == "3": delete_subject()
        elif choice == "4": view_subjects()
        elif choice == "0": break
        else: print("\nInvalid Choice!")
        pause()


def grade_menu():
    while True:
        print("\n--- INPUT GRADES ---")
        print("1. Add (pick subject)")
        print("2. Edit (pick subject)")
        print("3. Delete (pick subject)")
        print("4. View")
        print("0. Back")
        choice = input("Select: ")

        if choice == "1": add_grade()
        elif choice == "2": edit_grade()
        elif choice == "3": delete_grade()
        elif choice == "4": view_student_grades()
        elif choice == "0": break
        else: print("\nInvalid Choice!")
        pause()

if __name__ == "__main__":
    menu()