def add():
    '''Addition Program'''
    a = int(input('Enter the first number: '))
    b = int(input('Enter the second number: '))
    s = a+b
    print('The sum is',s)

add()

def add(x,y):
    '''Addition Program'''
    s = x+y
    print('The sum is',s)
    
# function calling
a = int(input('Enter the first number: '))
b = int(input('Enter the second Number: '))
add(a,b)
