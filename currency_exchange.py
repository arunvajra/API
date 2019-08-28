import requests

initial_value = float(input("ENTER THE CURRENCY AMOUNT \n"))
currency_base = input("ENTER THE CURRENCY BASE \n").upper()

currency_convert = input("WHICH CURRENCY DO YOU WANT TO CONVERT TO? \n").upper()

r = requests.get('https://api.exchangeratesapi.io/latest?base={}'.format(currency_base))


data = r.json() 
conversion = (initial_value) * data['rates'][currency_convert]

print("{} {} ---> {} {}".format(initial_value, currency_base, conversion, currency_convert))



