stocks = {"AAPL": 180, "TSLA": 250, "GOOG": 2800, "MSFT": 300, "AMZN": 3500}

portfolio = {}
total = 0

print("Available stocks and prices:", stocks)

while True:
    stock = input("Enter stock symbol (or 'done' to finish): ").upper()
    if stock == "DONE":
        break
    if stock not in stocks:
        print("Stock not found.")
        continue
    qty = int(input(f"Enter quantity for {stock}: "))
    portfolio[stock] = portfolio.get(stock, 0) + qty

print("\nYour Portfolio:")
for stock, qty in portfolio.items():
    value = stocks[stock] * qty
    total += value
    print(f"{stock}: {qty} shares = ${value}")

print("\nTotal Investment Value: $", total)

save = input("Do you want to save results to a file? (yes/no): ").lower()
if save == "yes":
    with open("portfolio.txt", "w") as f:
        for stock, qty in portfolio.items():
            value = stocks[stock] * qty
            f.write(f"{stock}: {qty} shares = ${value}\n")
        f.write(f"\nTotal Investment Value: ${total}")
    print("Portfolio saved to portfolio.txt")