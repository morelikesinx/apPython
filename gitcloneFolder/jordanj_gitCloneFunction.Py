def TriangleFunc():
a = float(input('Enter first side here'))
b = float(input('Enter second side here:'))
c = float(input('Enter third side here:'))

s = (a+b+c)/2
area = (s*(s-a)*(s-b)*(s-c)) * 0.5
print('The area of the triangle is %0.2f' %area)

TriangleFunc()

# read.me document
'This program is a triangle function. Enter any number into the three variables, A, B, and C.'
''