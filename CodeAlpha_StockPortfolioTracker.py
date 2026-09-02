stocks = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 420,
    "AMZN": 190
}

total = 0

print("===== STOCK PORTFOLIO TRACKER =====")

n = int(input("Enter number of stocks: "))

for i in range(n):
    stock = input("Enter stock name: ").upper()
    quantity = int(input("Enter quantity: "))

    if stock in stocks:
        value = stocks[stock] * quantity
        total += value
        print("Investment in", stock, "=", value)
    else:
        print("Stock not available.")

print("\nTotal Investment Value =", total)

with open("portfolio.txt", "w") as file:
    file.write("Stock Portfolio Tracker\n")
    file.write("Total Investment Value = " + str(total))

print("Portfolio saved to portfolio.txt")