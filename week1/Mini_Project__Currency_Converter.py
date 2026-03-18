#What it will do:
    #Show menu of currencies (USD, EUR, GBP, ZAR, etc.)
    #User picks "from" and "to" currency
    #User enters amount
    #Shows converted amount
    #Option to convert again or exit

#API: exchangerate-api.com - free, no sign-up needed!
#Everything you need:
    #API calls with requests ✅
    #.json() to get data ✅
    #Dictionaries to access data ✅
    #Menu loops ✅

import requests

def get_exchange_rates(from_currency):
    url = f"https://api.exchangerate-api.com/v4/latest/{from_currency}"
    response = requests.get(url)
    data = response.json()
    return data

def display_currencies(data):
    rates = data["rates"]
    for currency in rates:
        print(currency)

def convert_currency():
    from_currency = input("Enter the currency you want to convert from: \n")
    to_currency = input("Enter the currency you want to convert to: \n")
    amount = float(input("Amount: "))

    data = get_exchange_rates(from_currency)
    if "rates" not in data:
        print("Invalid currency code!")
        return
    else:
        rates = data["rates"]

    if to_currency not in rates:
        print(f"{to_currency} is not a valid currency!")
        return
    else:
        rate = rates[to_currency]

    converted = amount * rate

    print(f"{amount} {from_currency} = {converted} {to_currency}")




def main():
    while True:
        print("Currency Converter")
        print("1. Convert Currencies")
        print("2. Exit \n")

        choice = input("Please input an option: \n")

        if choice == "1":
            rates_data = get_exchange_rates("USD")
            display_currencies(rates_data)

            convert_currency()
        else:
            print("Goodbye!\n")


main()


