from enum import Enum
from locale import currency


class Conversion(Enum):
    USD_TO_EUR = "USD to EUR"
    EUR_TO_USD = "EUR to USD"
    USD_TO_GBP = "USD to GBP"
    GBP_TO_USD = "GBP to USD"
    EUR_TO_GBP = "EUR to GBP"
    GBP_TO_EUR = "GBP to EUR"


class Currency(Enum):
    USD = ("USD", "$")
    EUR = ("EUR", "€")
    GBP = ("GBP", "£")


converters = {
    Conversion.USD_TO_EUR: lambda amt: amt * 1.02,
    Conversion.EUR_TO_USD: lambda amt: amt * 0.98,
    Conversion.USD_TO_GBP: lambda amt: amt * 0.89,
    Conversion.GBP_TO_USD: lambda amt: amt * 1.12,
    Conversion.EUR_TO_GBP: lambda amt: amt * 0.87,
    Conversion.GBP_TO_EUR: lambda amt: amt * 1.15
}


conversions = {
    Currency.USD: [Conversion.USD_TO_EUR, Conversion.USD_TO_GBP],
    Currency.EUR: [Conversion.EUR_TO_USD, Conversion.EUR_TO_GBP],
    Currency.GBP: [Conversion.GBP_TO_USD, Conversion.GBP_TO_EUR]
}


def convert_currency(amt, converter):
    return converter(amt)


def do_exit():
    print(">> Exiting")
    raise SystemExit


def ask_currency():
    done = False
    while not done:
        print("Please select the currency:")
        print("1. USD")
        print("2. EUR")
        print("3. GBP")
        print("q. quit")
        user_input = input("> ")

        if user_input in ['1', '2', '3', 'q']:
            done = True
        else:
            print(">> Wrong selection\n")

    if user_input == 'q':
        do_exit()
    elif user_input == '1':
        return Currency.USD
    elif user_input == '2':
        return Currency.EUR
    else:
        return Currency.GBP


def ask_amount(currency):

    done = False
    while not done:
        user_input = input(f"Please type the amount of {currency.value[0]}: ")
        try:
            amount = float(user_input)
            done = True
        except Exception:
            print(f">> Wrong input: the amount must be a number")
    return amount


def ask_continue():
    done = False
    while not done:
        user_input = input("Perform another conversion (y/n): ")
        if user_input.lower() in ['y', 'n']:
            done = True
        else:
            print(">> Wrong selection\n")

    if user_input.lower() == 'n':
        return False
    else:
        return True


def print_conversions(currency, amount):
    print(f"{currency.value[1]}{amount}:")
    for conversion in conversions[currency]:
        print(f"  {conversion.value}: {convert_currency(amount, converters[conversion])}")


print("=== Currency Converter ===")
done = False
while not done:
    selected_currency = ask_currency()
    selected_amount = ask_amount(selected_currency)
    print_conversions(selected_currency, selected_amount)
    done = not ask_continue()
