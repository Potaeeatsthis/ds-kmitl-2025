class translator:

    def deciToRoman(self, num):
        roman_map = [
        (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
        (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
        (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')
        ]
        
        result = ""
        for value, symbol in roman_map:
            while num >= value:
                result += symbol
                num -= value
        return result

    def romanToDeci(self, s):
        return s

        
print(" *** Decimal to Roman ***")
num = int(input("Enter number to translate : "))

print(translator().deciToRoman(num))

print(num)
