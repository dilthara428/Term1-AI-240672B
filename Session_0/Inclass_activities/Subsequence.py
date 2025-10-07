# Function to check if x is a subsequence of y
def is_subsequence(x, y):
    i = j = 0
    while i < len(x) and j < len(y):
        if x[i] == y[j]:
            i += 1
        j += 1
    return i == len(x)


# Example test cases
x0 = "apple"
y1 = "adcsjncjsppaxjjnaxle"    # ✅ True (characters appear in order)
y2 = "bsdpple"                 # ❌ False
y3 = "paple"                   # ❌ False

print(is_subsequence(x0, y1))  # True
print(is_subsequence(x0, y2))  # False
print(is_subsequence(x0, y3))  # False