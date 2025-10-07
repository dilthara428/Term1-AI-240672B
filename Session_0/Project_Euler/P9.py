#Problem_09_Special Pythagorean triplet
#A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
#a^2 + b^2 = c^2
#For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.
#There exists exactly one Pythagorean triplet for which a + b + c = 1000.
#Find the product abc.
def find_pythagorean_triplet(sum_total):
    for a in range(1, sum_total):
        for b in range(a, sum_total - a):
            c = sum_total - a - b
            if a**2 + b**2 == c**2:
                return a * b * c
    return None
result = find_pythagorean_triplet(1000)
print(result)
