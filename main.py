from math import *
a, b, c = float(input()), float(input()), float(input())
D = b**2 - 4 * a * c
if D < 0:
    print("Нет корней")
elif D == 0:
    print(-b / (2 * a))
else:
    one = (-b + sqrt(D)) / (2 * a)
    two = (-b - sqrt(D)) / (2 * a)
    if one > two:
        print(two, one, sep = '\n')
    else:
        print(one, two, sep = '\n')
