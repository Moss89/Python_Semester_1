# Taking user input, and using mathematical expressions within print statements

# ratio 60:40
# tax rates 13.5% and 23%

amount = float(input("Please enter the sum of money you wish to calculate tax on: "))
# 60% of the amount multiplied by the low rate of 13.5%
amount_low_rate = (amount*.6) * 1.135
# 40% of the amount multiplied by the high rate of 23%
amount_high_rate = (amount*.4) * 1.23

# print the initial amount
print('The initial amount is: ', amount)
# lower tax rate amount (60%) with tax - lower tax rate amount
print('The lower tax rate amount is:', amount_low_rate - (amount*.6))
# higher tax rate amount (40%) with tax - higher tax rate amount
print('The higher tax rate amount is:', amount_high_rate - (amount*.4))
# amount with higher rate tax added to amount with lower rate tax, minus starting amount
print('The total tax is:', (amount_high_rate + amount_low_rate)-amount)
# adding the higher and lower amounts with tax applied
print('The total amount including taxes is:', amount_high_rate + amount_low_rate)






