students=[]
while True:
    print("\n--- Student System ---")
    print("1.Add Student")
    print("2.View Students")
    print("3.Delete Student")
    print("4.Exit")
    choice=input("Enter your choice:")
    if choice=="1":
        name=input("Enter name:")
        age=input("Enter age:")

        student={
            "name":name,
            "age":age
        }
        students.append(student)
        print("Student added!")
    elif choice=="2":
        if len(students)==0:
            print("No students found.")
        else:
            for i, s in enumerate(students):
                print(i,s["name"],s["age"])
    elif choice=="3":
        if len(students)==0:
            print("No students to delete.")
        else:
            for i, s in enumerate(students):
                print(i,s["name"])
            index=int(input("Enter index to delete:"))
            if 0<=index < len(students):
                students.pop(index)
                print("Deleted!")
            else:
                print("Invalid index.")
    elif choice=="4":
        print("Bye!")
        break
    else:
        print("Invalid choice, try again.")
        

