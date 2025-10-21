def shell_sort(arr) :
    n = len(arr)

    gap = n // 2

    while gap > 0 :
        for i in range(gap, n) :
            temp = arr[i]
            j = i

            while j >= gap and arr[j - gap] > temp :
                arr[j] = arr[j - gap]
                j -= gap

            arr[j] = temp

        gap //= 2
    return arr

inp = [int(i) for i in input("Enter Input : ").split()]
shell_sort(inp)
print(inp)
