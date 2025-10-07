#Problem_04: Largest palindrome product
#A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
#Find the largest palindrome made from the product of two 3-digit numbers.
def is_palindrome(n):
    return str(n) == str(n)[::-1]
def largest_palindrome_product(digits):
    largest = 0
    for i in range(10**(digits-1), 10**digits):
        for j in range(i, 10**digits):
            product = i * j
            if is_palindrome(product) and product > largest:
                largest = product
    return largest
print(largest_palindrome_product(3))
