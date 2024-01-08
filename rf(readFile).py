# Get user input
user_input = input("Enter some text: ")

# Write user input to a file
with open("user_input.txt", "w") as file:
    file.write(user_input)

# Read the file and print lines containing 'A' and 'E'
with open("user_input.txt", "r") as file:
    for line in file:
        if 'A' in line or 'E' in line:
            print(line.strip())
