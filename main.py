# make a function called add that adds as many numbers that are given
from zero import divide
def add(*args):
    total = 0
    for num in args:
        total += num
    return total


print(add(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
print("1 divided by 0 is", divide(1, 0))