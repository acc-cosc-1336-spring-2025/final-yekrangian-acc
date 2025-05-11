import os

class Stock:
    def __init__(self, symbol, company_name):
        self.__symbol = symbol
        self.__company_name = company_name

    def get_symbol(self):
        return self.__symbol

    def get_company_name(self):
        return self.__company_name

def get_stock_list():
    stock_list = []
    with open('stock_file.dat', 'r') as f:
        for line in f:
            parts = line.strip().split(' ', 1)
            if len(parts) == 2:
                symbol, company_name = parts
                stock_list.append(Stock(symbol, company_name))
    return stock_list

def main():
    while True:
        print("\nMenu:")
        print("1-Display stock purchase history")
        print("2-Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            stock_list = get_stock_list()
            print("\nStock Report")
            print(f"{'Company':<15} {'Symbol'}")
            for stock in stock_list:
                print(f"{stock.get_company_name():<15} {stock.get_symbol()}")
        elif choice == "2":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main() 