class Person:
    def __init__(self, name="", age=0):
        self.name = name
        self.age = age

    def display(self):
        print("\nPerson Details")
        print("Name:", self.name)
        print("Age:", self.age)


class Employee(Person):
    employee_count = 0

    def __init__(self, name="", age=0, employee_id="", salary=0):
        super().__init__(name, age)
        self.__employee_id = employee_id
        self.__salary = salary
        Employee.employee_count += 1
        print("Employee object created.")

    def __del__(self):
        print(f"Employee {self.name} deleted.")

    def get_employee_id(self):
        return self.__employee_id

    def get_salary(self):
        return self.__salary

    def set_employee_id(self, employee_id):
        self.__employee_id = employee_id

    def set_salary(self, salary):
        self.__salary = salary

    def display(self):
        super().display()
        print("Employee ID:", self.__employee_id)
        print("Salary:", self.__salary)


class Manager(Employee):
    def __init__(self, name, age, employee_id, salary, department):
        super().__init__(name, age, employee_id, salary)
        self.department = department

    def display(self):
        super().display()
        print("Department:", self.department)


class Developer(Employee):
    def __init__(self, name, age, employee_id, salary, language):
        super().__init__(name, age, employee_id, salary)
        self.language = language

    def display(self):
        super().display()
        print("Programming Language:", self.language)


employees = []

def add_employee():
    name = input("Enter Name: ")
    age = int(input("Enter Age: "))
    emp_id = input("Enter Employee ID: ")
    salary = float(input("Enter Salary: "))
    employees.append(Employee(name, age, emp_id, salary))
    print("Employee Added Successfully.")

def add_manager():
    name = input("Enter Name: ")
    age = int(input("Enter Age: "))
    emp_id = input("Enter Employee ID: ")
    salary = float(input("Enter Salary: "))
    dept = input("Enter Department: ")
    employees.append(Manager(name, age, emp_id, salary, dept))
    print("Manager Added Successfully.")

def add_developer():
    name = input("Enter Name: ")
    age = int(input("Enter Age: "))
    emp_id = input("Enter Employee ID: ")
    salary = float(input("Enter Salary: "))
    lang = input("Enter Programming Language: ")
    employees.append(Developer(name, age, emp_id, salary, lang))
    print("Developer Added Successfully.")

def update_employee():
    emp_id = input("Enter Employee ID to update: ")
    for emp in employees:
        if emp.get_employee_id() == emp_id:
            emp.name = input("Enter New Name: ")
            emp.age = int(input("Enter New Age: "))
            emp.set_salary(float(input("Enter New Salary: ")))
            if isinstance(emp, Manager):
                emp.department = input("Enter New Department: ")
            elif isinstance(emp, Developer):
                emp.language = input("Enter New Programming Language: ")
            print("Employee Updated Successfully.")
            return
    print("Employee Not Found.")

def delete_employee():
    emp_id = input("Enter Employee ID to delete: ")
    for emp in employees:
        if emp.get_employee_id() == emp_id:
            employees.remove(emp)
            Employee.employee_count -= 1
            print("Employee Deleted Successfully.")
            del emp
            return
    print("Employee Not Found.")

def display_employees():
    if not employees:
        print("No Employee Found.")
    else:
        for emp in employees:
            print("-" * 30)
            emp.display()

def subclass_check():
    print("Manager subclass of Employee:", issubclass(Manager, Employee))
    print("Developer subclass of Employee:", issubclass(Developer, Employee))

while True:
    print("\n===== Employee Management System =====")
    print("1. Add Employee")
    print("2. Add Manager")
    print("3. Add Developer")
    print("4. Update Employee")
    print("5. Delete Employee")
    print("6. Display Employees")
    print("7. Check Subclass")
    print("8. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_employee()
    elif choice == "2":
        add_manager()
    elif choice == "3":
        add_developer()
    elif choice == "4":
        update_employee()
    elif choice == "5":
        delete_employee()
    elif choice == "6":
        display_employees()
    elif choice == "7":
        subclass_check()
    elif choice == "8":
        print("Exiting Program...")
        break
    else:
        print("Invalid Choice!")
