#Name: Gabriel N Sa
#Date: 09.07.2018
#Description: Basic for loop test

#Recieving scores and returning the average grades:
def average(number_of_tests):
    accumulator = 0
    for counter in range(number_of_tests):
        accumulator += float(input('Enter the {}Â ºscore: '.format(counter+1)))
    return accumulator/number_of_tests

#Recieving number of tests:
def recieve_num_of_tests():
    number_of_tests = int(input('Enter the number of tests: '))
    return number_of_tests

#Main function:
number_of_tests = recieve_num_of_tests()
average = average(number_of_tests)
print('The average is {}'.format(average))
