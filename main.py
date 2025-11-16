import datetime
from pathlib import Path

#day = input('Enter the date in formate DD.MM.YY ')


def get_balance(data_file):
    """Get current balance.

    Reads database.txt file, calculates and returns total balance."""
    total_balance = 0
    with data_file.open(mode="r") as file_content:
        lines = file_content.readlines()

    for line in lines:
        try:
            amount = float(line)
        except ValueError:
            print("Could not parse Database file. Please check its content.")
            print("Quitting program...")
            quit()

        total_balance += amount
    return total_balance


def write_transaction(data_file, amount):
    """Write new transaction.

    Function writes new transaction amount to the file as a new line.
    Function returns updated total balance"""
    with data_file.open(mode="a") as file_content:
        file_content.write(str(amount) + "\n")
    return get_balance(data_file)


def main():
    """Main function."""

    data_file = Path.cwd() / "database.txt"
    if not data_file.exists():
        print("Database file doesn't exists, creating an empty file with zero balance")
        with data_file.open(mode="w") as file:
            file.write("0\n")

    balance = get_balance(data_file)
    print(f"Current balance: {balance}")

    while True:
        action = input("Input positive or negative amount or empty string to quit: ")
        if action == "":
            print("Exit program")
            quit()

        try:
            amount = float(action)
        except ValueError:
            print("Please, use the following formate 0.00.")
            continue

        # Saving new balance into file.
        balance = write_transaction(data_file, amount)

        if amount < 0:
            print(f"Amount {amount} is deducted. Actual balance: {balance}")
        else:
            print(f"Amount {amount} is added. Actual balance: {balance}")


if __name__ == "__main__":
    main()





