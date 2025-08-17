print("******** Parking Lot ********")
inp = input("Enter max of car / car in soi / operation : ").split('/')
max_cars = int(inp[0].strip())

cars_in_soi = [int(i) for i in inp[1].split(',')]

operation = inp[2].strip().split()
command = operation[0]
car_to_act = int(operation[1])

if command == "arrive" :
    if car_to_act in cars_in_soi:
        print(f"car {car_to_act} already in soi")
    elif len(cars_in_soi) >= max_cars:
        print(f"car {car_to_act} cannot arrive : Soi Full")
    else :
        cars_in_soi.append(car_to_act)
        print(f"car {car_to_act} arrive! : Add Car {car_to_act}")

if command == "depart" :
    if car_to_act not in cars_in_soi:
        print(f"car {car_to_act} cannot depart : Dont Have Car {car_to_act}")
    else :
        temp = []
        while cars_in_soi :
            poped_car = cars_in_soi.pop()
            if poped_car == car_to_act :
                print(f"car {car_to_act} depart ! : Car {car_to_act} was remove")
                break
            temp.append(poped_car)

        while temp :
            cars_in_soi.append(temp.pop())

print(cars_in_soi)
