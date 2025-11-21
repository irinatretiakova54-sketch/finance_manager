from datetime import datetime
from pathlib import Path


date_format = '%d.%m.%Y'


def get_balance(data_file):
    """Get current balance.

    Reads database.txt file, calculates and returns total balance."""
    total_balance = 0
    with data_file.open(mode="r") as file_content:
        lines = file_content.readlines()

    for line in lines:
        try:
            amount_str = line.split()[1]
            amount = float(amount_str)
        except ValueError:
            print("Could not parse Database file. Please check its content.")
            print("Quitting program...")
            quit()
        total_balance += amount
    return total_balance


def write_transaction(data_file, date, amount):
    """Write new transaction.

    Function writes new transaction amount to the file as a new line.
    Function returns updated total balance"""
    with data_file.open(mode="a") as file_content:
        file_content.write(
            datetime.strftime(date, date_format)
        )
        file_content.write(" ")
        file_content.write(str(amount) + "\n")

    return get_balance(data_file)


def main():
    """Main function."""

    data_file = Path.cwd() / "database.txt"
    if not data_file.exists():
        print("Database file doesn't exists, creating an empty file with zero balance")
        with data_file.open(mode="w") as file:
            pass

    balance = get_balance(data_file)
    print(f"Current balance: {balance}")

    while True:
        date_str = input("Input Data in formate DD.MM.YYYY or empty string to quit the program: ")
        if date_str == "":
            print("Exiting program...")
            quit()

        try:
            date = datetime.strptime(date_str, date_format)
        except ValueError:
            print("Wrong format. Please, use the following formate for the date DD.MM.YYYY ")
            continue

        amount_str = input("Input positive or negative amount or empty string to start over: ")
        if amount_str == "":
            print("Starting over...")
            continue

        try:
            amount = float(amount_str)
        except ValueError:
            print("Please, use the following formate 0.00.")
            continue

        # Saving new balance into file.
        balance = write_transaction(data_file, date, amount)

        if amount < 0:
            print(f"Amount {amount} is deducted. Actual balance: {balance}")
        else:
            print(f"Amount {amount} is added. Actual balance: {balance}")


if __name__ == "__main__":
    main()





