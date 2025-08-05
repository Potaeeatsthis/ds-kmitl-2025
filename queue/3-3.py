inp = input("Input: ")

vips = []
regulars = []

commands = inp.split(';')

for i in commands :
    parts = i.split()

    if parts[0] == "ARRIVE" : 
        if parts[2] == "VIP" :
            vips.append(parts[1])
        else :
            regulars.append(parts[1])

    elif parts[0] == "SERVE" :
        if vips :
            popped = vips.pop(0)
            print(f"Served: {popped}")

        elif regulars :
            popped = regulars.pop(0)
            print(f"Served: {popped}")
        
        else :
            print("No customers.")

    elif parts[0] == "VIEW" :
        join = vips + regulars 
        print(f"Queue: {join}")

    elif parts[0] == "EXIT" :
        print("Exiting.")
        break


