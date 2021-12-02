# Author: RTS 12/02/21

#def sum_to(n):
#     total = 0
#     for i in range(n + 1):
#           total += i
#return total

def sum_to(n):
    total = 0
    x = 0
    while x <= int(n):
        total += x
        x += 1

num = input("Enter a #: ")
print(sum_to(num))
