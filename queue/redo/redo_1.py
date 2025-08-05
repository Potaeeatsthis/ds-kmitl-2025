inp = input("Enter Input : ").split(',')

queue = []

for i in inp :

    part = i.split(' ')

    if part[0] == 'E' :
        queue.append(part[1])
        print(f"Add {part[1]} index is {len(queue)-1}")

    if part[0] == 'D' :
        if not queue :
            print(-1)
        else :
            popped = queue.pop(0)
            print(f"Pop {popped} size in queue is {len(queue)}")

if not queue :
    print("Empty")
else :
    print(f"Number in Queue is :  {queue}")
