print("******** Parking Lot ********")
inp = input("Enter max of car / car in soi / operation : ").split('/')

max_cars = int(inp[0].strip())

cars = [int(i) for i in inp[1].split(',')]

operation = inp[2].strip().split()
command = operation[0]
car_to_act = int(operation[1])

if command == "arrive" :
    if car_to_act in cars :
        print(f"car {car_to_act} already in soi")
    elif len(cars) >= max_cars :
        print(f"car {car_to_act} cannot arrive : Soi Full")
    else :
        cars.append(car_to_act)
        print(f"car {car_to_act} arrive! : Add Car {car_to_act}")

elif command == "depart" :
    if car_to_act not in cars :
        print(f"car {car_to_act} cannot depart : Dont Have Car {car_to_act}")
    else :
        cars.remove(car_to_act)
        print(f"car {car_to_act} depart ! : Car {car_to_act} was remove")

print(cars)
