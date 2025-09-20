class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def extend(self, other):
        if other.head:
            if not self.head:
                self.head, self.tail = other.head, other.tail
            else:
                self.tail.next = other.head
                self.tail = other.tail

    def is_empty(self):
        return self.head is None

    def __iter__(self):
        cur = self.head
        while cur:
            yield cur.data
            cur = cur.next

    def __str__(self):
        return " -> ".join(map(str, self))


def get_digit(number, d):
    return (number // (10 ** d)) % 10


def radix_sort_desc(values):
    if not values:
        return values

    max_val = max(values)
    rounds = len(str(max_val))

    for d in range(rounds):
        print("-" * 60)
        print(f"Round : {d+1}")

        buckets = [[] for _ in range(10)]
        for num in values:
            digit = get_digit(num, d)
            buckets[digit].append(num)

        for i in range(10):
            print(f"{i} : {' '.join(map(str, buckets[i]))}")

        # รวม bucket แบบ 9 -> 0 เพื่อให้ descending
        values = []
        for i in range(9, -1, -1):
            values.extend(buckets[i])

    return values, rounds


def radix_sort_with_negatives(ll):
    before = str(ll)

    positives = [x for x in ll if x >= 0]
    negatives = [-x for x in ll if x < 0]   # แปลงเป็นบวกชั่วคราว

    pos_sorted, rounds_pos = radix_sort_desc(positives) if positives else ([], 0)
    neg_sorted, rounds_neg = radix_sort_desc(negatives) if negatives else ([], 0)

    # ลบต้องกลับเป็นลบอีกครั้ง และ reverse ให้เรียงจาก -1 > -123 > -50385
    neg_sorted = [-x for x in reversed(neg_sorted)]

    result = pos_sorted + neg_sorted
    rounds = max(rounds_pos, rounds_neg)

    print("-" * 60)
    print(f"{rounds} Time(s)")
    print(f"Before Radix Sort : {before}")
    print(f"After  Radix Sort : {' -> '.join(map(str, result))}")


# -------- Main ----------
inp = list(map(int, input("Enter Input : ").split()))
ll = LinkedList()
for n in inp:
    ll.append(n)

radix_sort_with_negatives(ll)


