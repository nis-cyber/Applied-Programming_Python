numbers = []
for i in range(5):
    num = (input(f'Enter number {i + 1}: '))
    numbers.append(num)

with open('data.txt', 'w')as f:
    for i in numbers:
        f.write(f'{i}\n')

with open('data.txt','r')as f1, open('dest.txt','w')as f2:
    for i in f1:
        num = int(i)

        if num %2 ==0:
            f2.write(f'{num}\n')

