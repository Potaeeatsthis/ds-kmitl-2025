inp = input("Input: ")

vips = []
regulars = []

command = inp.split(';')

for i in command : 
    parts = i.split()

    if parts[0] == "ARRIVE" : 
        if parts[2] == "VIP" :
            vips.append(parts[1])
        else :
            regulars.append(parts[1])

    elif parts[0] == "SERVE" :
        if vips :
            print(f"Served: {vips.pop(0)}")

        elif regulars :
            print(f"Served: {regulars.pop(0)}")

        else :
            print("No customers.")

    elif parts[0] == "VIEW" :
        print(f"Queue: {vips + regulars}")

    elif parts[0] == "EXIT" :
        print("Exiting.")
        break
