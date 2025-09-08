# Stock Portfolio Tracker

def stock_portfolio_tracker():
    # Step 1: Hardcoded stock prices
    stock_prices = {
        "AAPL": 180,
        "TSLA": 250,
        "GOOG": 140,
        "MSFT": 300,
        "AMZN": 160
    }

    portfolio = {}
    total_value = 0

    print("📊 Welcome to Stock Portfolio Tracker 📊")
    print("Available stocks and prices (USD):")
    for stock, price in stock_prices.items():
        print(f"{stock} : ${price}")

    print("\nEnter your stock holdings (type 'done' to finish):")

    # Step 2: User input loop
    while True:
        stock_name = input("Enter stock symbol (AAPL/TSLA/GOOG/MSFT/AMZN or 'done'): ").upper()

        if stock_name == "DONE":
            break

        if stock_name not in stock_prices:
            print("⚠ Invalid stock symbol! Try again.")
            continue

        try:
            quantity = int(input(f"Enter quantity of {stock_name}: "))
        except ValueError:
            print("⚠ Please enter a valid number.")
            continue

        portfolio[stock_name] = portfolio.get(stock_name, 0) + quantity

    # Step 3: Calculate total investment
    print("\n📌 Your Portfolio Summary 📌")
    for stock, qty in portfolio.items():
        investment = qty * stock_prices[stock]
        total_value += investment
        print(f"{stock}: {qty} shares × ${stock_prices[stock]} = ${investment}")

    print(f"\n💰 Total Portfolio Value = ${total_value}")

    # Step 4 (Optional): Save result in text file
    save = input("\nDo you want to save the result to 'portfolio.txt'? (y/n): ").lower()
    if save == "y":
        with open("portfolio.txt", "w") as file:
            file.write("Your Portfolio Summary\n")
            for stock, qty in portfolio.items():
                investment = qty * stock_prices[stock]
                file.write(f"{stock}: {qty} shares × ${stock_prices[stock]} = ${investment}\n")
            file.write(f"\nTotal Portfolio Value = ${total_value}\n")
        print("✅ Portfolio saved to 'portfolio.txt'.")

# Run the tracker
stock_portfolio_tracker()
