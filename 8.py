print('Input lengths of the triangle sides:')
x = int(input())
y = int(input())
z = int(input())
if(x == y and x == z and y == z):
    print('equilateral triangle')

elif(x == y  or y == z):
    print('isosceles triangle')
else:
    print('scalene triangle')
