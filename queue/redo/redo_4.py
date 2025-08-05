employees, operations = input("Enter Input : ").split('/')

employees_map = {}
operation_list = []
main_queue = []

for i in employees :
    department, employee_id = i.strip().split(' ')
    department, employee_id = int(department), int(department)
    employees_map[employee_id] = department

for i in operations.split(',') :
    i = i.strip()
    if i == 'D' :
        operation_list.append('D',)
    elif i.startswith('E ') :
        employee_id  = int(i.split(' ')[1])
        operation_list.append(('E', employee_id)
