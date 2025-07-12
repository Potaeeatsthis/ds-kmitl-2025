def odd_list(ls):
    ods = []
    for i in ls :
        if i % 2 != 0 :
            ods.append(i)

    return ods

print(" ***Function Odd List***")
ls = [int(e) for e in input("Enter list numbers : ").split()]
opls = odd_list(ls)
print("Input list : ", ls, "\nOutput list : ", opls)
