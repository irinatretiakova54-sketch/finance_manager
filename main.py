import datetime
from pathlib import Path

#day = input('Enter the date in formate DD.MM.YY ')

data_file = Path.cwd() / "database.txt"
if not data_file.exists():
    print("Database file doesn't exists, creating an empty file with zero balance")
    with data_file.open(mode="w") as file:
        file.write("0")
data_file_content = data_file.read_text()
try:
    balance = float(data_file_content)
except ValueError:
    print("Could not parse Database file. Please check its content.")
    print("Quitting program...")
    quit()

print(f"Current balance: {balance}")

while True:
    action = input("Input positive or negative amount or empty string to quit: ")
    if action == "":
        print("Exit program")
        quit()

    try:
        action = float(action)
    except ValueError:
        print("Please, use the following formate 0.00.")
        continue

    balance = balance + action
    # Saving new balance into file.
    with data_file.open(mode="w") as file:
        file.write(str(balance))


    if action < 0:
        print(f"Amount {action} is deducted. Actual balance: {balance}")
    else:
        print(f"Amount {action} is added. Actual balance: {balance}")




# if data_file.exists():
#     with data_file.open(mode="a") as file:
#         contents = file.write("Happy new year!")
#         print(f"File{data_file.name} is now open")
#     print(f"File{data_file.name} is now close")
