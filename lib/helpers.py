from models.department import Department
from models.employee import Employee


def exit_program():
    print("Goodbye!")
    exit()

# We'll implement the department functions in this lesson


def list_employees():
    employees = Employee.get_all()
    for employee in employees:
        print(employee)


def find_employee_by_name():
    name = input("Enter the employee's name: ")
    employee = Employee.find_by_name(name)
    print(employee) if employee else print(f"Employee {name} not found")


def find_employee_by_id():
    id_ = input("Enter the employee's id: ")
    employee = Employee.find_by_id(id_)
    print(employee) if employee else print(f"Employee {id_} not found")


def create_employee():
    name = input("Enter the employee's name: ")
    job_title = input("Enter the employee's job title: ")
    dept_id = input("Enter the employee's department id:")

    try:
        employee = Employee.create(name, job_title, dept_id)
        print(f"Success: {employee}")
    except Exception as exc:
        print("Error creating employee: ", exc)


def update_employee():
    id_ = input("Enter the employee's id: ")
    employee = Employee.find_by_id(id_)

    if not employee:
        print(f"Employee {id_} not found")
        return

    try:
        new_name = input("Enter the employees's new name: ")
        employee.name = new_name

        new_title = input("Enter the employee's new job title: ")
        employee.job_title = new_title

        new_dept = input("Enter the employees's new department id: ")
        employee.department_id = new_dept

        employee.update()
        print(f"Success: {employee}")

    except Exception as exc:
        print("Error updating employee: ", exc)


def delete_employee():
    id_ = input("Enter the employee's id: ")
    employee = Employee.find_by_id(id_)

    if employee:
        employee.delete()
        print(f"Employee {id_} deleted")
    else:
        print(f"Employee {id_} not found")


def list_department_employees():
    dept_id = input("Enter the department's id: ")
    department = Department.find_by_id(dept_id)

    if not department:
        print(f"Department {dept_id} not found")
        return

    employees = department.employees()

    for employee in employees:
        print(employee)