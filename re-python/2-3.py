def RANGE(*args):
    if len(args) == 1:
       start, stop, step = 0.0, float(args[0]), 1.0
    elif len(args) == 2:
       start, stop, step = float(args[0]), float(args[1]), 1.0
    elif len(args) == 3:
        start, stop, step = float(args[0]), float(args[1]), float(args[2])
    else:
       return tuple()
   
    if step == 0:
       return tuple()

    result = []
    current_value = float(start)
    
    if step > 0:
        while current_value < stop:
            result.append(round(current_value, 3))
            current_value += step
    else:
        while current_value > stop:
            result.append(round(current_value, 3))
            current_value += step

    return tuple(result)

print('*** New Range ***')
n = [float(i) for i in input('Enter Input : ').split()]
if len(n) == 1:
    k = RANGE(n[0])
    print(RANGE(n[0]))
elif len(n) == 2:
    print(RANGE(n[0], n[1]))
elif len(n) == 3:
    print(RANGE(n[0], n[1], n[2]))