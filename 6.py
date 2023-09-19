x = int(input())
y = int(input())

def myFunction(x, y):
    sum = x + y
    if (sum >= 15 and sum <= 20):
        return 20
    else:
        return sum
    
print(myFunction(x, y))
