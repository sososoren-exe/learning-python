#Grade Tracker - Menu-driven student grade management system

students = {}

while True:
    print("    Grade Tracker    ")
    print("1. Add student")
    print("2. View all students")
    print("3. View class average")
    print("4. Find Highest/Lowest grade")
    print("5. Delete student")
    print("6. Clear all students")
    print("7. Exit")

    choice = input("Choose option: ")

    if choice == "1":
        new_name = input("Name: ")
        grade = float(input("Grade: "))
        students[new_name] = grade
        print(f"Added {new_name}!\n")
    
    elif choice == "2":
        print("Here are your students: ")
        for name, grade in students.items():
            print(f"{name}: {grade}")
    
    elif choice == "3":
        total = 0
        print("Here is your class average:")
        for value in students.values():
            total = total + value
            average = total/len(students)
        print(f"{average}\n")
    
    elif choice == "4":
        highest_name = ""
        highest_grade = 0

        for name, grade in students.items():
            if grade > highest_grade:
                highest_grade = grade
                highest_name = name
        print(f"Highest: {highest_name} with {highest_grade}")
        
        lowest_name = ""
        lowest_grade = 100

        for name, grade in students.items():
            if grade < lowest_grade:
                lowest_grade = grade
                lowest_name = name
        print(f"Lowest: {lowest_name} with {lowest_grade} \n")
    
    elif choice == "5":
        print("Here are your students:")
        for name, grade in students.items():
            print(f"{name}: {grade}")
            
        del_student = input("Which student would you like to delete? ")
        if del_student in students:
            print("Student exists!")
            del students[del_student]
            print(f"Student: {del_student} deleted! \n")
        else:
            print("No student found. \n")
    
    elif choice == "6":
        clear = input("Are you sure you want to clear all students? (Yes/No) ")
        if clear.lower() == "Yes":
            students.clear()
            print("Students cleared successfully!")
        else:
            print("Clearing cancelled. \n")

    elif choice == "7":
        print("Program Exited. \n")
        break
