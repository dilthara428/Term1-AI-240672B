#Problem 03: Largest prime factor
#The prime factors of 13195 are 5, 7, 13 and 29.
#What is the largest prime factor of the number 600851475143 ?

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
def largest_prime_factor(n):
    largest = None
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0 and is_prime(i):
            largest = i
            while n % i == 0:
                n //= i
    if n > 1 and is_prime(n):
        largest = n
    return largest
print(largest_prime_factor(600851475143))

