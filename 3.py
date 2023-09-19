n = int(input("Input a dog's age in human years: "))
if n <= 2:
    age = n*10,5

else:
    age = 21 + (n-2)*4

print("The dog's age in dog's years is", age)
