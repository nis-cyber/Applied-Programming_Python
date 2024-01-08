# import random
#
# winner = 0
#
# user_choice=(int(input("Enter the number as 1 for Rock, 2 for Paper and 3 for Scissor: ")))
#
# def computerRandomNumberGen():
#     return random.randint(1,3)
#
#
# def displayComputerChoice(computer_choice):
#     if computer_choice == 1:
#         print('Computer have choose R')
#     elif computer_choice ==2:
#         print('Computer have choose P')
#     else:
#         print('Computer have choose S')
#
# def displayUserChoice(user_choice):
#     if user_choice ==1:
#         print('You have choose R')
#     elif user_choice ==2:
#         print('You have choose P')
#     elif user_choice ==3:
#         print('You have choose S')
#     else:
#         print('Error!! choose valid number')
#
#
# def userInfo():
#     name = input('Enter your name: ')
#     address = input('Enter your address: ')
#     phone_number = int(input('Enter your phone number: '))
#
#     return name,address,phone_number
#
# def determineWinnerOfRPS(user_choice,computer_choice):
#     winner = None
#     if user_choice ==1 and computer_choice==3:
#         winner = 'user wins'
#
#     elif user_choice ==2 and computer_choice ==1:
#         winner = 'user wins'
#     elif user_choice ==3 and computer_choice ==2:
#         winner = 'user wins'
#     elif user_choice ==computer_choice:
#         print('Its a Tie Play Again!!')
#     else:
#         winner = 'Computer wins'
#
#     return winner
#
#
# def display_static_info(winner,name,address,phone_number):
#     with open('result.txt', 'w') as f:
#         f.write(f'''{winner}has won the game
#         name: {name} \naddress: {address}\n phone number: {phone_number}''')
#
#
#
#
# name,address,phone_number = userInfo()
# displayUserChoice(user_choice)
# computer_choice = computerRandomNumberGen()
# displayComputerChoice(computer_choice)
# winner = determineWinnerOfRPS(user_choice,computer_choice)
# print(winner)
# display_static_info(winner,name,address,phone_number)
#
#
#



import random

result = []
names = []
addresses = []
phone_numbers = []




user_choice=(int(input("Enter the number as 1 for Rock, 2 for Paper and 3 for Scissor: ")))

def computerRandomNumberGen():
    return random.randint(1,3)


def displayComputerChoice(computer_choice):
    if computer_choice == 1:
        print('Computer have choose R')
    elif computer_choice == 2:
        print('Computer have choose P')
    else:
        print('Computer have choose S')

def displayUserChoice(user_choice):
    if user_choice ==1:
        print('You have choose R')
    elif user_choice ==2:
        print('You have choose P')
    elif user_choice ==3:
        print('You have choose S')
    else:
        print('Error!! choose valid number')


def userInfo():
    name = input('Enter your name: ')
    address = input('Enter your address: ')
    phone_number = (input('Enter your phone number: '))

    return name,address,phone_number

def determineWinnerOfRPS(user_choice,computer_choice):
    winner = None
    if user_choice ==1 and computer_choice==3:
        winner = 'user wins'

    elif user_choice ==2 and computer_choice ==1:
        winner = 'user wins'
    elif user_choice ==3 and computer_choice ==2:
        winner = 'user wins'
    elif user_choice ==computer_choice:
        print('Its a Tie Play Again!!')
    else:
        winner = 'Computer wins'

    return winner


def display_static_info(results,names,addresses,phone_numbers):
    with open('result.txt', 'w') as f:
        f.write(f'Results:\n')
        for i, result in enumerate(results):
            f.write(f'Round {i+1}: {result}\n')
        f.write(f'\nPlayers:\n')
        for i, name in enumerate(names):
            f.write(f'Player {i+1}: {name} from {addresses[i]} with phone number {phone_numbers[i]}\n')




name, address, phone_number = userInfo()

names.append(name)
addresses.append(address)
phone_numbers.append(phone_number)

displayUserChoice(user_choice)
computer_choice = computerRandomNumberGen()
displayComputerChoice(computer_choice)
winner = determineWinnerOfRPS(user_choice, computer_choice)
print(winner)
result.append(winner)

display_static_info(result, names, addresses, phone_numbers)

