def quick_sort(arr, pivot_type):
    def sort(a, left, right):
        if left >= right:
            return 0
        if pivot_type == "first":
            pivot_index = left
        elif pivot_type == "last":
            pivot_index = right
        else:
            pivot_index = (left + right) // 2
        a[left], a[pivot_index] = a[pivot_index], a[left]
        pivot = a[left]
        i = left + 1
        for j in range(left + 1, right + 1):
            if a[j] < pivot:
                a[i], a[j] = a[j], a[i]
                i += 1
        a[left], a[i - 1] = a[i - 1], a[left]
        comp = right - left
        comp += sort(a, left, i - 2)
        comp += sort(a, i, right)
        return comp
    arr_copy = arr[:]
    return sort(arr_copy, 0, len(arr_copy) - 1)

print("*** Quick sort ***")
nums = list(map(int, input("Enter a sequence of integers : ").split()))

first_comp = quick_sort(nums, "first")
last_comp = quick_sort(nums, "last")
middle_comp = quick_sort(nums, "middle")

print("\nNumber of comparisons for each pivot strategy:")
print(f"First Pivot: {first_comp} comparisons")
print(f"Last Pivot: {last_comp} comparisons")
print(f"Middle Pivot: {middle_comp} comparisons")
print("===== End of program =====")

