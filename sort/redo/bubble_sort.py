def bubble_sort(arr) :
    n = len(arr)

    for i in range (n - 1) :
        swapped = False
        for j in range(0, n - i - 1) :
            if arr[j] > arr[j + 1] :
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True

        if not swapped :
            break

try:
    inp_str = input("Enter Input : ").split()
    inp = [int(i) for i in inp_str]

    print("List before sorting:", inp)
    bubble_sort(inp)
    print("List after sorting:", inp)

except ValueError:
    print("Invalid input. Please enter numbers separated by spaces.")
