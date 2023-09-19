n = []
counter = 0
sum = 0.0
print('Input some numbers:')
while n != 0:
    n = int(input())
    counter += 1
    sum+= n
print('Averega value of this number is', sum/ (counter-1))

