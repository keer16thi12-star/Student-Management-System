students = {}

def add_student():
    roll = input("Enter Roll Number: ")
    name = input("Enter Name: ")
    marks = float(input("Enter Marks: "))
    students[roll] = {"name": name, "marks": marks}
    print("Student added successfully.\n")

def view_students():
    if not students:
        print("No student records found.\n")
    else:
        for roll, info in students.items():
            print(f"Roll: {roll}, Name: {info['name']}, Marks: {info['marks']}")
        print()

def search_student():
    roll = input("Enter Roll Number to search: ")
    if roll in students:
        info = students[roll]
        print(f"Found: Name: {info['name']}, Marks: {info['marks']}\n")
    else:
        print("Student not found.\n")

def update_student():
    roll = input("Enter Roll Number to update: ")
    if roll in students:
        name = input("Enter new Name: ")
        marks = float(input("Enter new Marks: "))
        students[roll] = {"name": name, "marks": marks}
        print("Student updated successfully.\n")
    else:
        print("Student not found.\n")


# MAIN MENU
while True:
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        search_student()
    elif choice == "4":
        update_student()
    elif choice == "5":
        break
    else:
        print("Invalid choice\n")
