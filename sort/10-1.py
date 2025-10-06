def special_bubble_sort(data_list):
    n = len(data_list)
    step_count = 1
    
    # The outer loop controls the passes. We need at most n-1 passes.
    for i in range(n - 1):
        swapped_in_pass = False
        last_moved_value = None
        
        # The inner loop performs comparisons and swaps for one pass.
        for j in range(n - 1 - i):
            if data_list[j] > data_list[j + 1]:
                # Record the value at the lower index before it moves.
                last_moved_value = data_list[j]
                
                # Perform the swap.
                data_list[j], data_list[j + 1] = data_list[j + 1], data_list[j]
                swapped_in_pass = True
        
        # After a pass, check the results to decide what to print.

        # Condition 1: If no swaps happened, the list is sorted.
        if not swapped_in_pass:
            print(f"last step : {data_list} move[None]")
            return # Exit the function early
        
        # Condition 2: If this was the last possible sorting pass.
        # This will also result in a sorted list.
        if i == n - 2:
            print(f"last step : {data_list} move[{last_moved_value}]")
            return

        # Otherwise, it was a regular intermediate step.
        print(f"{step_count} step : {data_list} move[{last_moved_value}]")
        step_count += 1

# --- Main execution block ---
inp_str = input("Enter Input : ").split()
numbers = []
for s in inp_str:
    numbers.append(int(s))

special_bubble_sort(numbers)
