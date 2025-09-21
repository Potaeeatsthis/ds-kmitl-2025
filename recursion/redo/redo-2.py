def len_str(mystr) :
    if mystr == '' :
        return 0
    return 1 + len_str(mystr[1:])

def sep(mystr, index = 1) :
    if mystr == '' :
        return ''

    if index % 2 == 1 :
        return mystr[0] + '*' + sep(mystr[1:], index + 1)
    else :
        return mystr[0] + '~' + sep(mystr[1:], index + 1)

print(" *** Length of string (Recursion) ***")
input = input("Enter Input : ")
print(sep(input))
print(f"length of '{input}' is {len_str(input)}")
