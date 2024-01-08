class Employee:
    def __init__(self, emp_name, emp_id, emp_salary, emp_department):
        self.emp_name = emp_name
        self.emp_id = emp_id
        self.emp_salary = emp_salary
        self.emp_department = emp_department

    def calculate_emp_salary(self, hours_worked):
        # If the number of hours worked is more than 50, calculate overtime
        if hours_worked > 50:
            overtime = hours_worked - 50
            self.emp_salary += overtime * 20  # Assuming an overtime rate of $20 per hour

    def assign_department(self, new_department):
        self.emp_department = new_department

    def print_employee_details(self):
        print("Employee Details:")
        print("Employee Name:", self.emp_name)
        print("Employee ID:", self.emp_id)
        print("Employee Salary:", self.emp_salary)
        print("Employee Department:", self.emp_department)


# Sample Employee Data
employees_data = [
    {"name": "RAHUL", "id": "E7876", "salary": 50000, "department": "ACCOUNTING"},
    {"name": "PRAKASH", "id": "E7499", "salary": 45000, "department": "RESEARCH"},
    {"name": "ADAM", "id": "E7900", "salary": 50000, "department": "SALES"},
    {"name": "SMITH", "id": "E7698", "salary": 55000, "department": "OPERATIONS"}
]

# Create Employee instances and print their details
for emp_data in employees_data:
    emp = Employee(emp_data["name"], emp_data["id"], emp_data["salary"], emp_data["department"])
    emp.calculate_emp_salary(55)  # Assuming 55 hours worked
    emp.assign_department("HR")  # Assuming the department is changed to HR
    emp.print_employee_details()
    print()
