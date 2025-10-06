def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

try:
    left_str, right_str = input("Enter Input : ").split('/')
    main_list = [int(n) for n in left_str.split()]
    targets = [int(n) for n in right_str.split()]
except ValueError:
    print("Invalid input format. Please check your input.")
    exit()

sorted_list = insertion_sort(main_list)

for target in targets:
    first_greater_value = None
    for num in sorted_list:
        if num > target:
            first_greater_value = num
            break  # Exit the inner loop as we've found our answer
    if first_greater_value is not None:
        print(first_greater_value)
    else:
        print("No First Greater Value")

