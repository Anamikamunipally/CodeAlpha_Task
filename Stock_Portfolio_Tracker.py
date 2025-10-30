def stock_portfolio_tracker():
    stock_prices = {"AAPL": 180, "TSLA": 250, "GOOG": 140, "MSFT": 300}
    portfolio = {}
    total_investment = 0

    n = int(input("Enter number of stocks you own: "))

    for _ in range(n):
        stock = input("Enter stock symbol (AAPL/TSLA/GOOG/MSFT): ").upper()
        qty = int(input(f"Enter quantity of {stock}: "))
        if stock in stock_prices:
            portfolio[stock] = qty
            total_investment += stock_prices[stock] * qty
        else:
            print("Invalid stock symbol!")

    print("\nYour Portfolio:")
    for stock, qty in portfolio.items():
        print(f"{stock}: {qty} shares worth ${stock_prices[stock] * qty}")

    print("\nTotal Investment Value = $", total_investment)

    with open("portfolio.txt", "w") as file:
        file.write(f"Total Investment Value = ${total_investment}\n")

if __name__ == "__main__":
    stock_portfolio_tracker()
