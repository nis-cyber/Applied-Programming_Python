import random


def initialDisplay():
    head = '''Hi, This is Sunway Lotttery system'''

    # Generate a random two-digit number for the lottery
    lottery = random.randint(10, 99)
    print('lottery',lottery)

    # Prompt the user to enter a two-digit number
    guess = int(input("Enter your two-digit number: "))
    return head, guess, lottery


def calculation(guess, lottery):
    # Check if the user's input matches the lottery in the exact order
    if guess == lottery:
        prize = 10000
    # Check if all the digits in the user's input match all the digits in the lottery number
    elif sorted(str(guess)) == sorted(str(lottery)):
        prize = 3000
    # Check if one digit in the user's input matches a digit in the lottery number
    elif any(str(digit) in str(lottery) for digit in str(guess)):
            prize = 1000
    else:
        prize = 0

    return prize



def finaldisplay(head, prize):
    print(head)
    print(f"Your prize is: ${prize}")
    return prize, head


# Call the functions
head, guess, lottery = initialDisplay()
prize = calculation(guess, lottery)
finaldisplay(head, prize)