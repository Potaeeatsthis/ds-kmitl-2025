inp = input("Enter Input : ")

queue = []

command = inp.split(',')

for i in command :
    part = i.split()

    if part[0] == 'E' :
        queue.append(part[1])
        print(f"Add {part[1]} index is {len(queue)-1}")

    elif part[0] == 'D' :
        if not queue :
            print("-1")
        else :
            print(f"Pop {queue.pop(0)} size in queue is {len(queue)}")

if queue :
    print(f"Number in Queue is :  {queue}")
else :
    print("Empty")
