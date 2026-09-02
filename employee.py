import mysql.connector

# Connect to MySQL
con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="3411",
    database="employee_db"
)

cursor = con.cursor()

while True:

    print("\n===== Employee Management System =====")
    print("1. Add Employee")
    print("2. View Employees")
    print("3. Update Employee")
    print("4. Delete Employee")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        emp_id = int(input("Enter Employee ID: "))
        name = input("Enter Employee Name: ")
        salary = float(input("Enter Salary: "))

        cursor.execute(
            "INSERT INTO employee VALUES (%s, %s, %s)",
            (emp_id, name, salary)
        )

        con.commit()
        print("Employee added successfully!")

    elif choice == 2:
        cursor.execute("SELECT * FROM employee")

        for employee in cursor.fetchall():
            print(employee)

    elif choice == 3:
        emp_id = int(input("Enter Employee ID: "))
        salary = float(input("Enter New Salary: "))

        cursor.execute(
            "UPDATE employee SET salary=%s WHERE id=%s",
            (salary, emp_id)
        )

        con.commit()
        print("Employee updated successfully!")

    elif choice == 4:
        emp_id = int(input("Enter Employee ID: "))

        cursor.execute(
            "DELETE FROM employee WHERE id=%s",
            (emp_id,)
        )

        con.commit()
        print("Employee deleted successfully!")

    elif choice == 5:
        print("Thank you!")
        break

    else:
        print("Invalid choice!")

cursor.close()
con.close()