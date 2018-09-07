#Name: Gabriel N Sa
#Date: 09.07.2018
#Description: Simple Calculator.

def menu():
    print('***************Menu***************')
    print('(1) -> Sum')
    print('(2) -> Subtraction')
    print('(3) -> Multiplication')
    print('(4) -> Division') 
    print('(5) -> Potenciation') 
    print('(6) -> Root') 
    print('(7) -> Second degree equation')
    print('Any other number to quit.')

def sum_num():
    a = float(input('Enter a: '))
    b = float(input('Enter b: '))
    print('The reult: {:.2f}'.format(a+b))
    print()

def subtraction():
    a = float(input('Enter a: '))
    b = float(input('Enter b: '))
    print('The reult: {:.2f}'.format(a-b))
    print()

def multiplication():
    a = float(input('Enter a: '))
    b = float(input('Enter b: '))
    print('The reult: {:.2f}'.format(a*b))
    print()

def division():
    a = float(input('Enter a: '))
    b = float(input('Enter b: '))
    print('The reult: {:.2f}'.format(a/b))
    print()

def potenciation():
    print('a^b')
    a = float(input('Enter a: '))
    b = float(input('Enter b: '))
    print('The reult: {:.2f}'.format(a**b))
    print()

def root_num():
    a = float(input('Enter the root index: '))
    b = float(input('Enter the basis: '))
    print('The reult: {:.2f}'.format(b**(1/a)))
    print()

def scnd_dgree_eq():
    print('a*x²+ b*x + c = 0')
    a = float(input('Enter a: '))
    b = float(input('Enter b: '))
    c = float(input('Enter c: '))

    delta = (b**2) - 4*a*c
    if(delta >= 0):
        first_root = (-1)*b + delta**(1/2)
        first_root /= (2*a)
        print('X1: {:.2f}'.format(first_root))
        second_root = (-1)*b - delta**(1/2)
        second_root /= (2*a)
        print('X2: {:.2f}'.format(second_root))
        print()
    else:
        delta = ((-1)*delta)**(1/2)
        root_integer = ((-1)*b)/(2*a)
        root_complex = delta/(2*a)
        print('X1: {:.2f} + {:.2f}i'.format(root_integer, root_complex))
        print('X2: {:.2f} - {:.2f}i'.format(root_integer, root_complex))
        print()

#Main Function:
loop = True

while(loop):
    menu()
    option = int(input('Type your option: '))
    if(option == 1):
        sum_num()
    elif(option == 2):
        subtraction()
    elif(option == 3):
        multiplication()
    elif(option == 4):
        division()
    elif(option == 5):
        potenciation()
    elif(option == 6):
        root_num()
    elif(option ==7):
        scnd_dgree_eq()
    else:
        loop = False
