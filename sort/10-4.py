def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

l = [e for e in input("Enter Input : ").split()]
if l[0] == 'EX':
    Ans = "Insertion Sort"
    print("Extra Question : What is a suitable sort algorithm?")
    print("   Your Answer : " + Ans)
else:
    l = list(map(int, l))
    unsorted_list = []
    for num in l:
        unsorted_list.append(num)

        list_to_sort = unsorted_list[:]

        insertion_sort(list_to_sort)

        n = len(list_to_sort)
        median = 0.0
        if n % 2 == 1:  # Odd number of elements
            median = float(list_to_sort[n // 2])
        else:  # Even number of elements
            mid1 = list_to_sort[n // 2 - 1]
            mid2 = list_to_sort[n // 2]
            median = (mid1 + mid2) / 2.0

        print(f"list = {unsorted_list} : median = {median}")
