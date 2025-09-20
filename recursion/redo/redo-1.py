def natural_sum(n):
    if n <= 1 :
        return 1
    else :
        return n + natural_sum(n - 1)

print(" *** Natural sum ***")
num = int(input("Enter number : ")) 
total_sum = natural_sum(num)

num_str = " + ".join(str(i) for i in range(1, num + 1))

print(f"{num_str} = {total_sum}")
print("===== End of program =====")
