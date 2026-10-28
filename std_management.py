print ("TEST:correct file is running") 
students = {}

def calculate_grade(marks):
    if marks >= 90:
        return "A"
    elif marks >= 80:
        return "B"
    elif marks >=70:
        return "C"
    elif marks >=60:
        return "D"
    else:
        return "F"

def add_student():
    name = input("Enter student name: ").strip()

    if not name:
        print("Name cannot be empty.")
        return
    
    if name in students:
        print("student already exists.")
        return
    try:
        marks = float(input("Enter marks (0-100): "))

        if not 0 <= marks <=100:
            print ("marks must be between 0 and 100.")
            return
        students[name] = {
            "marks": marks,
            "grade":calculate_grade(marks)
        } 
        print(f"{name} added successfully!")
    except ValueError:
        print("please enter a valid number.")

def view_students():
    if not students:
        print("no students registered.")
        return
    for name, details in students.items():
        print(
            f"Name: {name} | "
            f"Marks: {details['marks']} |"
            f"Grade: {details['grade']}"
        )

def search_students():
    name = input ("Enter student name to search: ").strip()

    if name in students:
        details = students[name]
        print(f"Name: {name}")
        print(f"Marks: {details['marks']}")
        print(f"Grade: {details['grade']}")
    else:
        print("student not found.")

while True:
    print("\n--- Student management system ---")
    print("1. Add students")
    print("2. view all students")
    print("3. search students")
    print("4. Exit")

    choice = input("choose an option: ").strip()
    print("DEBUG:", repr(choice))
    
    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        search_students()
    elif choice == "4":
      print("Goodbye!")
      break
else:
    print("invalid choice. Try again.")   
       



            
