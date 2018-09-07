#Name: Gabriel N Sa
#09.07.2018
#Desciption - Basic if statement test.

#Getting temperature values
def get_values():
    temperature = float(input('Enter the temperature in Celcius: '))
    return temperature

#Checking temperature:
def check_temperature(temperature):
    if(temperature > 35):
        print("It's very hot!")
    elif(temperature > 28 and temperature <= 35):
        print("It's hot!")     
    elif(temperature > 20 and temperature <= 28):
        print("It's nice!")
    elif(temperature > 10 and temperature <= 20):
        print("It's cold")
    else:
        print("It's very cold")

#Check the exit condition:
def check_exit_condition():
    option = input("Type 's' if you want to finish the program: ")
    print()
    if(option == 's'):
        return False
    else:
        return True

#Main function:
loop = True
while loop:
    temperature = get_values()
    check_temperature(temperature)
    loop = check_exit_condition()

