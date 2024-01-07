def display_triangle_pattern(rows):
    for i in range(1, rows+1):
        for j in range(i):
            print("*", end="")
        print()

# Enter the user for the number of rows
rows = int(input("Enter the number of rows: "))

# Call the function to display the triangle pattern
display_triangle_pattern(rows)
