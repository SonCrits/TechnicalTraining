import api


def is_Employee(func):
    def wrapper(employee_list):
        func(employee_list)
        print("Done")
    return wrapper

@is_Employee
def display_employee(employee_list):
    for employee in employee_list:
        print(f"{employee} is employee")

#ham nay chi de loc employee
def filter_employee_age_less(employee_list):
    employee_list_age = []
    for employee in employee_list:
        if employee.get('age') <= 20:
            employee_list_age.append(employee.get('name'))
    return employee_list_age

# 3 hàm trên đều truyền vào tham số giống nhau
#nhưng không sử dụng decorator lồng được
# vì employee list của filter employee khác vs 2 hàm đầu tiên
#có cách nào để làm được không ạ?


a = filter_employee_age_less(api.employee_list)
b = display_employee
b(a)
