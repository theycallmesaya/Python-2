a = float(input('Input first number:'))
b = float(input('Input second number:'))
c = float(input('Input third number:'))
if((a > b and a < c) or (a > c and a < b )):
    print('The median is', a)
if((b > a and b < c) or (b > c and b < a )):
    print('The median is', b)
if((c > b and c < a) or (c >  a and c < b )):
    print('The median is', c)

