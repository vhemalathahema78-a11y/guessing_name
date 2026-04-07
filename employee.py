employees = []

def add_employee():
    name = input("Enter employee name: ")
    emp_id = input("Enter employee ID: ")
    dept = input("Enter department: ")
    
    employees.append({"name": name, "id": emp_id, "dept": dept})
    print("Employee added successfully!")

def view_employees():
    if not employees:
        print("No employees found")
    else:
        for emp in employees:
            print(emp)

def search_employee():
    emp_id = input("Enter employee ID to search: ")
    for emp in employees:
        if emp["id"] == emp_id:
            print("Employee found:", emp)
            return
    print("Employee not found")

def delete_employee():
    emp_id = input("Enter employee ID to delete: ")
    for emp in employees:
        if emp["id"] == emp_id:
            employees.remove(emp)
            print("Employee deleted")
            return
    print("Employee not found")

while True:
    print("\n1.Add 2.View 3.Search 4.Delete 5.Exit")
    choice = input("Enter choice: ")

    if choice == "1":
        add_employee()
    elif choice == "2":
        view_employees()
    elif choice == "3":
        search_employee()
    elif choice == "4":
        delete_employee()
    elif choice == "5":
        break
    else:
        print("Invalid choice")
