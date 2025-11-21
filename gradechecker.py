import sys

students = {}          # {student_name: student_name}
subjects = {}          # {subject_name: subject_name}
grades = {}            # {student_name: {subject_name: grade}}

def pause():
    input("\nPress Enter to continue...")

# STUDENTS
def add_student():
    name = input("Enter student name: ").strip() 
    #strip removes spaces before and after the string bale if ever may nag input ng " felix" for example tapos naread ng program, magiging "felix" na lang siya
    if name in students:
        print("\nStudent already exists!")
        return
    students[name] = name
    print(f"\nStudent added successfully: {name}")

def edit_student():
    name = input("Enter student name to edit: ").strip()
    if name not in students:
        print("\nStudent not found!")
        return

    new_name = input("Enter new name: ").strip()

    if name in grades:
        grades[new_name] = grades.pop(name)

    students.pop(name)
    students[new_name] = new_name

    print("\nStudent updated!")

def delete_student():
    name = input("Enter student name to delete: ").strip()
    if name not in students:
        print("\nStudent not found!")
        return

    students.pop(name)
    grades.pop(name, None)

    print("\nStudent deleted!")

def view_students():
    if not students:
        print("\nNo students available.")
        return

    print("\n--- STUDENTS LIST ---")
    for name in students:
        print(name)

# SUBJECTS
def add_subject():
    subject = input("Enter subject name: ").strip()
    if subject in subjects:
        print("\nSubject already exists!")
        return

    subjects[subject] = subject
    print("\nSubject added!")

def edit_subject():
    subject = input("Enter subject name to edit: ").strip()
    if subject not in subjects:
        print("\nSubject not found!")
        return

    new_subject = input("Enter new subject name: ").strip()

    # Update grade keys
    for s in grades:
        if subject in grades[s]:
            grades[s][new_subject] = grades[s].pop(subject)

    subjects.pop(subject)
    subjects[new_subject] = new_subject

    print("\nSubject updated!")

def delete_subject():
    subject = input("Enter subject name to delete: ").strip()
    if subject not in subjects:
        print("\nSubject not found!")
        return

    subjects.pop(subject) #pop is remove ong dont forget to explain to felixz

    for s in grades:
        grades[s].pop(subject, None)

    print("\nSubject deleted!")

def view_subjects():
    if not subjects:
        print("No subjects available.")
        return

    print("\n--- SUBJECTS LIST ---")
    for name in subjects:
        print(name)

# GRADES
def pick_student():
    if not students:
        print("\nNo students available!")
        return None
    view_students()
    return input("Enter student name: ").strip()

def pick_subject():
    if not subjects:
        print("\nNo subjects available!")
        return None
    view_subjects()
    return input("Enter subject name: ").strip()

def add_grade():
    student = pick_student()
    if not student or student not in students:
        print("\nInvalid student!")
        return

    subject = pick_subject()
    if not subject or subject not in subjects:
        print("\nInvalid subject!")
        return

    grade = input("Enter grade: ").strip()
    grades.setdefault(student, {})[subject] = grade
    print("\nGrade added!")

def edit_grade():
    student = pick_student()
    if not student or student not in grades:
        print("\nNo grades for this student.")
        return

    subject = pick_subject()
    if not subject or subject not in grades[student]:
        print("\nNo grade for this subject.")
        return

    grade = input("Enter new grade: ").strip()
    grades[student][subject] = grade
    print("\nGrade updated!")

def delete_grade():
    student = pick_student()
    if not student or student not in grades:
        print("\nNo grades for this student.")
        return

    subject = pick_subject()
    if not subject or subject not in grades[student]:
        print("\nGrade not found.")
        return

    grades[student].pop(subject)
    print("\nGrade deleted!")

def view_all_grades():
    if not students:
        print("\nNo students available.")
        return

    print("\n===== ALL STUDENTS' GRADES =====")

    for sName, studentName in students.items():
        print(f"\n--- {studentName} ---")

        # If the student has no grades
        if sName not in grades or not grades[sName]:
            print("  No grades available.")
            continue

        # Show each subject + grade
        for sub, g in grades[sName].items():
            print(f"  {sub}: {g}")


# MENUS
def menu():
    while True:
        print("\n===== GRADE CHECKER SYSTEM =====")
        print("1. Manage Students")
        print("2. Manage Subjects")
        print("3. Input Grades")
        print("4. View Grades")
        print("5. Exit")

        choice = input("Select an option: ").strip()

        if choice == "1":
            student_menu()
        elif choice == "2":
            subject_menu()
        elif choice == "3":
            grade_menu()
        elif choice == "4":
            view_all_grades()
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

        choice = input("Select: ").strip()

        if choice == "1":
            add_student()
        elif choice == "2":
            edit_student()
        elif choice == "3":
            delete_student()
        elif choice == "4":
            view_students()
        elif choice == "0":
            break
        else:
            print("\nInvalid Choice!")
        pause()

def subject_menu():
    while True:
        print("\n--- MANAGE SUBJECTS ---")
        print("1. Add")
        print("2. Edit")
        print("3. Delete")
        print("4. View")
        print("0. Back")

        choice = input("Select: ").strip()

        if choice == "1":
            add_subject()
        elif choice == "2":
            edit_subject()
        elif choice == "3":
            delete_subject()
        elif choice == "4":
            view_subjects()
        elif choice == "0":
            break
        else:
            print("\nInvalid Choice!")
        pause()

def grade_menu():
    while True:
        print("\n--- INPUT GRADES ---")
        print("1. Add (pick subject)")
        print("2. Edit (pick subject)")
        print("3. Delete (pick subject)")
        print("0. Back")
        choice = input("Select: ")

        if choice == "1":
            add_grade()
        elif choice == "2":
            edit_grade()
        elif choice == "3":
            delete_grade()
        elif choice == "0":
            break
        else:
            print("\nInvalid Choice!")

        pause()


if __name__ == "__main__":
    menu()
