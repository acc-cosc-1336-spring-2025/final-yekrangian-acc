def create_multiplication_table():
    table = []
    for i in range(1, 6):  # Rows: 1 to 5
        row = []
        for j in range(1, 11):  # Columns: 1 to 10
            row.append(i * j)
        table.append(row)
    return table

def display_multiplication_table(table):
    for row in table:
        print(' '.join(str(x) for x in row))

def main():
    while True:
        table = create_multiplication_table()
        display_multiplication_table(table)
        cont = input("\nDo you want to display the table again? (y/n): ").strip().lower()
        if cont != 'y':
            print("Exiting program.")
            break

if __name__ == "__main__":
    main() 