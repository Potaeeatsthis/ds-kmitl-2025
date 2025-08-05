class Queue :
    def __init__(self) :
        self.items = [] 

    def enqueue(self, item) :
        self.items.append(item)

    def dequeue(self) :
        if not self.is_empty() :
            return self.items.pop(0)
        return None

    def is_empty(self) :
        return len(self.items) == 0

    def size(self) :
        return len(self.items)

    def __str__(self) :
        return str(self.items)

main = Queue()
cashier_1 = Queue()
cashier_2 = Queue()

inp = input("Enter people : ")

for i in inp : 
    main.enqueue(i) 

minute = 0 

cashier_1_timer = 0
cashier_2_timer = 0

max_queue = 5 

while True :
    minute += 1

    if not cashier_1.is_empty() :
        cashier_1_timer += 1 
        if cashier_1_timer % 3 == 0 :
            cashier_1.dequeue()
    elif cashier_1.is_empty() :
        cashier_1_timer = 0

    if not cashier_2.is_empty() :
        cashier_2_timer += 1 
        if cashier_1_timer % 2 == 0 :
            cashier_2.dequeue()
    elif cashier_2.is_empty() :
        cashier_2_timer = 0

    if not main.is_empty() :
        if cashier_1.size() < max_queue :
            move_to_1 = main.dequeue()
            cashier_1.enqueue(move_to_1)
        else :
            move_to_2 = main.dequeue()
            cashier_2.enqueue(move_to_2)

    if main.is_empty() :
        print(f"{minute} {main} {cashier_1} {cashier_2}")
        break 

    print(f"{minute} {main} {cashier_1} {cashier_2}")
