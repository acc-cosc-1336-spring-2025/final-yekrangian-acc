class Stock:
    def __init__(self, symbol, company_name):
        self.__symbol = symbol
        self.__company_name = company_name

    def get_symbol(self):
        return self.__symbol

    def get_company_name(self):
        return self.__company_name

def stock_purchase_history():
    # Create 5 Stock instances
    stock1 = Stock("AAPL", "Apple Inc")
    stock2 = Stock("CAT", "Caterpillar")
    stock3 = Stock("EK", "Eastman Kodak")
    stock4 = Stock("GOOG", "Google")
    stock5 = Stock("MSFT", "Microsoft")

    # Add to dictionary
    stocks = {
        stock1.get_symbol(): stock1,
        stock2.get_symbol(): stock2,
        stock3.get_symbol(): stock3,
        stock4.get_symbol(): stock4,
        stock5.get_symbol(): stock5,
    }

    # Display as table
    print("\nStock list")
    print(f"{'Symbol':<8} {'Company Name'}")
    for symbol, stock in stocks.items():
        print(f"{stock.get_symbol():<8} {stock.get_company_name()}")

def main():
    while True:
        print("\nMenu:")
        print("1-Display stock purchase history")
        print("2-Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            stock_purchase_history()
        elif choice == "2":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main() 