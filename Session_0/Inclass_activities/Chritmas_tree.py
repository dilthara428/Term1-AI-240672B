# 🎄 Python program to print a Christmas Tree

# height of the tree
height = 7

# printing the leaves
for i in range(height):
    # print spaces
    for j in range(height - i - 1):
        print(" ", end="")
    # print stars
    for k in range(2 * i + 1):
        print("*", end="")
    print()

# printing the trunk
for i in range(2):
    for j in range(height - 1):
        print(" ", end="")
    print("|")
