#Name: Gabriel N Sa
#Date: 09.07.2018
#Description: Recursive fibonacci sequence.

#Recursive fibonnaci sequence:
def fibonacci(final_term, next_num = 1, previous_num = 1):
    if(final_term > 1):
        if(next_num == 1):
            print(previous_num)
        print(next_num)
        return fibonacci(final_term-1, next_num+previous_num, next_num)

#Main function:
term = int(input('Type the number of terms you want from fibonacci: '))
fibonacci(term)
