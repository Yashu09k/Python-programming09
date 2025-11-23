#Student add karna (name + age + marks)

#Sare students dekhna

#Highest marks wala student

#Total students count
Students=[]
while True:
    print("Welcome to Student-Management-System")
    print("1:Add Student")
    print("2: View All Students")
    print("3: See The Topper (Highest-Marks)")
    print("4: Count All Students")
    print("5: Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        name = input("Enter name: ")
        age = int(input("Enter age: "))
        marks = int(input("Enter marks: "))

        Students.append([name, age, marks])
        print("Student added successfully!")
    elif choice==2:
        print("\n Students List")
        for s in Students:
            print(f"name:{s[0]}, Age:{s[1]},Marks:{s[2]}")
    elif choice == 3:
        if len(Students) == 0:
            print("No students available.")
        else:
            topper = max(Students, key=lambda x: x[2])
            print(f"\nTopper: {topper[0]} (Marks: {topper[2]})")
    elif choice==4:
        print(f"Total Students:{len(Students)}")
    elif choice==5:
        print("Thank You!")
    else:
        print("Invalid Choice")
