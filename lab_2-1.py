# Author: RTS 12/01/21

def sum_to(x):
    total = 0
    for value in range(int(x) + 1):
        total += value
    return total

xy = input("Enter a number: ")
print(sum_to(xy))
