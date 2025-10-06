def custom_sort_positives(data):
    positives = []
    for num in data:
        if num >= 0:
            positives.append(num)

    n = len(positives)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if positives[j] > positives[j + 1]:
                positives[j], positives[j + 1] = positives[j + 1], positives[j]

    positive_index = 0
    for i in range(len(data)):
        if data[i] >= 0:
            data[i] = positives[positive_index]
            positive_index += 1

    return data

input_str = input("Enter Input : ").split()
numbers = []
for s in input_str:
    numbers.append(int(s))

sorted_list = custom_sort_positives(numbers)

output = []
for num in sorted_list:
    output.append(str(num))

print(" ".join(output))
