def len_str(mystr) :
    if mystr == "" :
        return 0
    else :
        return 1 + len_str(mystr[:-1])

def sep(txt, index=1):
    if txt == "":
        return ""
    
    if index % 2 == 1:
        return txt[0] + "*" + sep(txt[1:], index + 1)
    else:
        return txt[0] + "~" + sep(txt[1:], index + 1)

print(" *** Length of string (Recursion) ***")
input = input("Enter Input : ")
print(sep(input))
print(f"length of '{input}' is {len_str(input)}")