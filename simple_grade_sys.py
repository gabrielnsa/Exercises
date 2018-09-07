#Name: Gabriel N Sa
#Date: 09.07.2018
#Description: Basic for loop test

#Recieving scores and returning the average grades:
def average(number_of_tests):
    accumulator = 0
    for counter in range(number_of_tests):
        accumulator += float(input('Enter the {}º score: '.format(counter+1)))
    return accumulator/number_of_tests

#Recieving number of tests:
def recieve_num_of_tests():
    number_of_tests = int(input('Enter the number of tests: '))
    return number_of_tests

#Checking approval:
def check_approval(average, presence_index):
    if(average >= 7):
        print('APPROVED')
    elif((average >= 3 and average <7) and presence_index >= 75):
        print('TO SUMMER SCHOOL')
    elif(average < 3):
        print('NOT APPROVED BY AVERAGE GRADE')
    else:
        print('NOT APPROVED BY PRESENCE')

#Calculate presence index:
def compute_presence_index():
    number_of_classes = int(input('Enter the total number of classes: '))
    missed_classes = int(input('Enter the number of missed classes by the student: '))
    presence_index = (missed_classes/number_of_classes)*100
    return (100 - presence_index)

#Main function:
number_of_tests = recieve_num_of_tests()
average = average(number_of_tests)
presence_index = compute_presence_index()
check_approval(average, presence_index)
