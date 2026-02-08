students = []
def add_students():
    name=input("Enter student name: "       )
    marks=int(input("Enter student marks: "))
    students.append((name, marks))
    print("Student added successfully!")    
def view_students():
    if not students:
        print("No students found.")
    else:
        print("Student List:")
        for name, marks in students:
            print(f"Name: {name}, Marks: {marks}")
while True:
    print("1. Add Student")
    print("2. View Students")
    print("3. Exit")
    choice=int(input("Enter your choice: "))
    if choice==1:
        add_students()
    elif choice==2:
        view_students()
    elif choice==3:
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please try again.")
