class Employee:
    def __init__(self, emp_id, emp_name, emp_salary, emp_department):
        self.emp_id = emp_id
        self.emp_name = emp_name
        self.emp_salary = emp_salary
        self.emp_department = emp_department

    def calculate_emp_salary(self, hours_worked):
        overtime = 0
        if hours_worked > 50:
            overtime = hours_worked - 50
        overtime_amount = overtime * (self.emp_salary / 50)
        total_salary = self.emp_salary + overtime_amount
        return total_salary
    def emp_assign_department(self, new_department):
        self.emp_department = new_department
    def print_employee_details(self):
        print(f"Employee ID: {self.emp_id}")
        print(f"Employee Name: {self.emp_name}")
        print(f"Employee Salary: {self.emp_salary}")
        print(f"Employee Department: {self.emp_department}")
employees = [
    Employee("E7876", "ADAMS", 50000, "ACCOUNTING"),
    Employee("E7499", "JONES", 45000, "RESEARCH"),
    Employee("E7900", "MARTIN", 50000, "SALES"),
    Employee("E7698", "SMITH", 55000, "OPERATIONS")
]
employees[0].emp_assign_department("IT")
employees[0].print_employee_details()
print(f"Total Salary (with overtime): {employees[0].calculate_emp_salary(55)}")
