inp = input("Enter max of car / car in soi / operation : ").split('/')

max_slot = int(inp[0].strip())

car_in_soi = [int(i) for i in inp[1].split(',')]

operation = inp[2].strip().split()
command = operation[0]
car_to_act = int(operation[1])

if command == "arrive" :
	if car_to_act in car_in_soi :
		print(f"car {car_to_act} already in soi")
	elif len(car_in_soi) >= max_slot :
		print(f"car {car_to_act} cannot arrive : Soi Full")
	else :
		car_in_soi.append(car_to_act)
		print(f"car {car_to_act} arrive! : Add Car {car_to_act}")

elif command == "depart" :
	if car_to_act not in car_in_soi :
		print(f"car {car_to_act} cannot depart : Dont Have Car {car_to_act}")
	else :
		temp = []
		while car_in_soi :
			popped_car = car_in_soi.pop()
			if popped_car == car_to_act :
				print(f"car {car_to_act} depart ! : Car {car_to_act} was remove")
				break
			else :
				temp.append(popped_car)

		while temp :
			car_in_soi.append(temp.pop())
				
print(car_in_soi)
