import api


def is_Employee(func):
    def wrapper(employee_list):
        #func(employee_list)
        employee = func(employee_list)
        for e in employee:
            print(f"{e} is employee")
    return wrapper

@is_Employee
def filter_employee_age_less(employee_list):
    employee_list_age = []
    for employee in employee_list:
        if employee.get('age') <= 20:
            employee_list_age.append(employee.get('name'))
    return employee_list_age  


a = filter_employee_age_less(api.employee_list)
