#Name: Gabriel N Sa
#Date: 09.07.2018
#Description: Recursive factorial.

#Recursive Factorial
def factorial(n):
    if(n<2):
        return 1;
    return n*factorial(n-1)

n = int(input('Factorial from: '))
print(factorial(n))
