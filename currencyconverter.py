def convert(amount, rate):
    return amount * rate

amount = float(input("Enter the amount in USD: "))
rate = float(input("Enter the exchange rate to EUR: "))
print(f"{amount} USD is {convert(amount, rate)} EUR")
