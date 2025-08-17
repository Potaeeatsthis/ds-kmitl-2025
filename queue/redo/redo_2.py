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
cashier1 = Queue()
cashier2 = Queue()

inp = input("Enter people : ")

for i in inp :
    main.enqueue(i)

minute = 0

cashier_1_timer = 0
cashier_2_timer = 0

cashier_1_max = 5

while True :
    minute += 1

    if not cashier1.is_empty() :
        cashier_1_timer += 1
        if cashier_1_timer % 3 == 0 :
            cashier1.dequeue()
            if cashier1.is_empty() :
                cashier_2_timer = 0

    if not cashier2.is_empty() :
        cashier_2_timer += 1
        if cashier_2_timer % 2 == 0 :
            cashier2.dequeue()
            if cashier2.is_empty() :
                cashier_2_timer = 0

    if not main.is_empty() :
        if cashier1.size() < cashier_1_max :
            cashier1.enqueue(main.dequeue())
        else :
            cashier2.enqueue(main.dequeue())

    if main.is_empty() :
        print(f"{minute} {main} {cashier1} {cashier2}")
        break

    print(f"{minute} {main} {cashier1} {cashier2}")
