# Author: RTS 12/01/21

def sum_to(num):
    total = 0
    for value in range(int(num) + 1):
        total += value
    return total

number = input("Enter a #: ")
print(sum_to(number))
