#Problem_05: Smallest multiple
#2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
#What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
import math     
def lcm(a, b):
    return abs(a * b) // math.gcd(a, b)

def smallest_multiple(n):
    multiple = 1
    for i in range(1, n + 1):
        multiple = lcm(multiple, i)
    return multiple
print(smallest_multiple(20))

