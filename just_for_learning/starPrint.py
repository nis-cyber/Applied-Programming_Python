# Prompt the user to enter a number
num = int(input("Enter a number: "))

# Use a nested for loop to construct the pattern
for i in range(num):
    for j in range(i + 1):
        print("*", end=" ")
    print()

for i in range(num - 1, 0, -1):
    for j in range(i):
        print("*", end=" ")
    print()


