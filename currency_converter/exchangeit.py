"""
User interface for module currency

When run as a script, this module prompts the user for two currencies and amount.
It prints out the result of converting the first currency to the second.

"""

import currency

src = input('3-letter code for original currency: ')
dst = input('3-letter code for the new currency: ')
amount = input('Amount of the original currency: ')
# Convert input string formatted to float
amt = float(amount)
# Call exchange function to compute exchange value
exchange = currency.exchange(src, dst, amt)
# Round exchange value to 3 decimals
amt_rounded = round(exchange, 3)
# Construct print statement
result = 'You can exchange ' + str(amt) + ' ' + src + ' for ' + str(amt_rounded) + ' ' + dst + '.'
# Print result
print(result)