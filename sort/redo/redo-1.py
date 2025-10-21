def bubble_sort(arr) :
    n = len(arr)

    swap_count = 1

    for i in range(n-1) :
        swapped = False
        last_swapped = None
        for j in range(0, n - i - 1) :
            if arr[j] > arr[j + 1] :
                last_swapped = arr[j]
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped :
            print(f"last step : {arr} move[None]")
            return

        if i == n - 2 :
            print(f"last step : {arr} move[{last_swapped}]")
            return

        print(f"{swap_count} step : {arr} move[{last_swapped}]")
        swap_count += 1

inp = [int(i) for i in input("Enter Input : ").split()]
bubble_sort(inp)
