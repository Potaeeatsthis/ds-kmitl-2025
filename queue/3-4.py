employee, operations = input("Enter Input : ").split('/')

employee_map = {}
operations_list = []
main_queue = []

for i in employee.split(',') :
    department, employee_id = i.strip().split(' ')
    department, employee_id = int(department), int(employee_id)
    employee_map[employee_id] = department

for i in operations.split(','):
    i = i.strip()
    if i == 'D' :
        operations_list.append('D',)
    elif i.startswith("E ") :
        employee_id = int(i.split(' ')[1])
        operations_list.append(('E', employee_id))

print(employee_map)
for i in operations_list :
    op_type = i[0]

    if op_type == 'D' :
        if not main_queue :
            print("Empty")
        else :
            print(main_queue.pop(0))

    elif op_type == 'E' :
        employee_to_add = i[1]
        place_new_emp = employee_map[employee_to_add]

        pos = -1 

        for j in range(len(main_queue) -1 , -1, -1 ) :
            current_emp = main_queue[j]
            if employee_map[current_emp] == place_new_emp :
                pos = j + 1
                break

        if pos == -1 :
            main_queue.append(employee_to_add)
        else :
            main_queue.insert(pos, employee_to_add)

