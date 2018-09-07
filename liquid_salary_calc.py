#Name: Gabriel N Sa
#Date: 09.07.2018
#Description: Calculates the liquid salary of a pearson.

#Compute the tax value
def tax_value(brute_salary, tax):
    value = (brute_salary*tax)/100
    return value

#Layout Division:
def div():
    print('*'*50)

#Main function: 

#Recieving Values:
brute_salary = float(input('Enter the value of your brute salary: '))
tax_income = float(input('Enter the percentage of the income tax: '))
tax_retirement = float(input('Enter the percentage of the retirement tax: '))
bonus_housing = float(input('Enter the value of your housing assistance: '))
bonus_alimentation = float(input('Enter the value of your alimentation assistance: '))

#Output menu: 
print()
div()
print('{:30}{}{:.2f}'.format('Brute Slary','=  ', brute_salary))
div()
print('Taxes:')
print('{:30}{}{:.2f}'.format('Income Tax','=  ', tax_value(brute_salary, tax_income)))
print('{:30}{}{:.2f}'.format('Social Previdence','=  ', tax_value(brute_salary, tax_retirement)))
print('')
print('Bonuses:')
print('{:30}{}{:.2f}'.format('Housing Assistance','=  ', bonus_housing))
print('{:30}{}{:.2f}'.format('Alimentation Assistance','=  ', bonus_alimentation))
div()
liquid_salary = (brute_salary + bonus_housing + bonus_alimentation) - (tax_value(brute_salary, tax_income) + tax_value(brute_salary, tax_retirement))
print('{:30}{}{:.2f}'.format('Liquid Salary','=  ', liquid_salary))

