def employee_data():
    sentinal = 999
    employee_number: str = input("Enter Employee Number \n")
    employee_name: str = input("Enter Employee Name \n")
    employee_basic_salary: int = int(input("Enter Employee Basic Salary \n"))
    employee_department: str = input("Enter Employee Department \n")
    if employee_department not in ["sales", "marketing", "administration", "management"] and employee_number == sentinal:
        print("Employee doesn't belong to valid department")
        exit()
    else:
        print("\n")
        print("Employee Number is " + employee_number)
        print("Employee Name is " + employee_name)
        print("Employee Basic Salary is " + str(employee_basic_salary))
        print("Employee Department is " + str(employee_department))
        print("Employee VA is " + str(salary(employee_department, employee_basic_salary)[0]))
        print("Employee DA is " + str(salary(employee_department, employee_basic_salary)[1]))
        print("Employee GS is " + str(salary(employee_department, employee_basic_salary)[2]))
        print("Employee CPP is " + str(salary(employee_department, employee_basic_salary)[3]))
        print("Employee Federal Tax is " + str(salary(employee_department, employee_basic_salary)[4]))
        print("Employee NetSalary is " + str(salary(employee_department, employee_basic_salary)[5]))
        print("\n")


def salary(employee_department, employee_basic_salary):
    if employee_department == "management":
        vacation_allowance = float((employee_basic_salary * 20) / 100)
        dental_allowance = float((employee_basic_salary * 20) / 100)
        gross_salary = float(employee_basic_salary + vacation_allowance + dental_allowance)
        cpp = float((gross_salary * 15) / 100)
        federal_tax = float((gross_salary * 12) / 100)
        net_salary = float(gross_salary - cpp - federal_tax)
        return vacation_allowance, dental_allowance, gross_salary, cpp, federal_tax, net_salary
    elif employee_department == "sales" or employee_department == "marketing":
        vacation_allowance = float((employee_basic_salary * 10) / 100)
        dental_allowance = float((employee_basic_salary * 7) / 100)
        gross_salary = float(employee_basic_salary + vacation_allowance + dental_allowance)
        cpp = float((gross_salary * 10) / 100)
        federal_tax = float((gross_salary * 12) / 100)
        net_salary = float(gross_salary - cpp - federal_tax)
        return vacation_allowance, dental_allowance, gross_salary, cpp, federal_tax, net_salary
        print("\n")
    elif employee_department == "administration":
        vacation_allowance = 0
        dental_allowance = float((employee_basic_salary * 7) / 100)
        gross_salary = float(employee_basic_salary + vacation_allowance + dental_allowance)
        cpp = float((gross_salary * 10) / 100)
        federal_tax = float((gross_salary * 12) / 100)
        net_salary = float(gross_salary - cpp - federal_tax)
        return vacation_allowance, dental_allowance, gross_salary, cpp, federal_tax, net_salary
        print("\n")
    else:
        exit()


if __name__ == '__main__':
    employee_count = int(input("Enter employee count \n"))
    while employee_count:
        employee_data()
