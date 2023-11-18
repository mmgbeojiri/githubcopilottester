#create a divide function that has two parameters
import math
def divide(x, y):
    try:
        return x / y
    except ZeroDivisionError:
        #if x is greater than 0, return infinity
        if y == 0:
            if x > 0:
                return math.inf
            if x < 0:
                return -math.inf
            if x == 0:
                return 0
        #check to see if y is negative zero "-0"
        if y == -0.0:
            if x > 0:
                return -math.inf
            if x < 0:
                return math.inf
            if x == 0:
                return -0.0