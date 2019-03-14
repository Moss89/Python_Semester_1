# Taking user input, then printing strings and numericals, multiplying floats

# Convert user inputted string to float
currency_euro = float(input('Please enter an amount in euro to be converted to dollars: '))
euro_dollar_rate = 1.17
# Exchange rate as of 18/09/2018

# print initial amount by the exchange rate
print(currency_euro, 'Euro to Dollars = ', (currency_euro * euro_dollar_rate))
