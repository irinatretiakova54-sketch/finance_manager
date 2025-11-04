import datetime
#day = input('Enter the date in formate DD.MM.YY ')
balance = 0
while True:
    action = input("Input positive or negative amount or empty string to quit: ")
    if action == "":
        print("Exit program")
        quit()

    action = int(action)
    balance = balance + action
    if action < 0:
        print(f"Amount {action} is deducted. Actual balance: {balance}")
    else:
        print(f"Amount {action} is added. Actual balance: {balance}")