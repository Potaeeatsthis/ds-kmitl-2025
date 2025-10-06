class Data:
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __str__(self):
        return "({0}, {1})".format(self.key, self.value)

class hash:
    def __init__(self, table_size, max_collision):
        self.table_size = table_size
        self.max_collision = max_collision
        self.table = [None] * self.table_size
        self.elements_count = 0
        self.full_message_printed = False

    def add(self, key, value):
        if self.elements_count == self.table_size:
            if not self.full_message_printed:
                print("This table is full !!!!!!")
                self.full_message_printed = True
            return False

        data_item = Data(key, value)
        initial_index = sum(ord(c) for c in data_item.key) % self.table_size
        
        if self.table[initial_index] is None:
            self.table[initial_index] = data_item
            self.elements_count += 1
            return True

        collision_count = 0
        for i in range(1, self.table_size * 2): # Iterate more than enough to be safe
            collision_count += 1
            
            print(f"collision number {collision_count} at {initial_index}")

            if collision_count == self.max_collision:
                print("Max of collisionChain")
                return True

            new_index = (initial_index + i * i) % self.table_size
            
            if self.table[new_index] is None:
                self.table[new_index] = data_item
                self.elements_count += 1
                return True
            
            # This is to handle the next collision print message correctly
            initial_index = new_index

        print("Max of collisionChain")
        return True

    def print_table(self):
        for i, item in enumerate(self.table):
            print(f"#{i + 1}\t{item}")
        print("---------------------------")


print("***** Fun with hashing *****")
inp_str = input("Enter Input : ").split('/')
table_params = inp_str[0].split()
data_to_add = inp_str[1].split(',')

table_size = int(table_params[0])
max_collision = int(table_params[1])

h = hash(table_size, max_collision)

for item in data_to_add:
    key, value = item.split()
    should_print = h.add(key, value)
    if should_print:
        h.print_table()
