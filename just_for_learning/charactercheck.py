from datetime import date
date= date.today()

def mainDisplay():
    # Print the welcome message
    print(f'''
    Welcome to Sunway Character Check System
            Maitidevi, Kathmandu \t {date}''')
    # Prompt the user to enter a string
    string = input("Enter a string: ")

    # Initialize the counters for each type of character
    upper_count = 0
    lower_count = 0
    special_count = 0
    numeric_count = 0

    # Iterate through each character in the string
    for i in string:
        # Check if the character is an uppercase letter
        if i.isupper():
            upper_count += 1
        # Check if the character is a lowercase letter
        elif i.islower():
            lower_count += 1
        # Check if the character is a special character
        elif not i.isalnum():
            special_count += 1
        # Otherwise, the character must be a numeric character
        else:
            numeric_count += 1
    # Print the results
    print("Number of upper case letters:", upper_count)
    print("Number of lower case letters:", lower_count)
    print("Number of special characters:", special_count)
    print("Number of numeric characters:", numeric_count)
    print("Thank you for the visit.")

mainDisplay()
