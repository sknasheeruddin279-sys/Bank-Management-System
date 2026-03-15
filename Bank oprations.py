def create_account():
    acc_no = input("Enter Account Number: ")
    name = input("Enter Account Holder Name: ")
    balance = "0"

    with open("accounts.txt", "a") as file:
        file.write(f"{acc_no},{name},{balance}\n")

    print("Account created successfully!")


def view_accounts():
    try:
        with open("accounts.txt", "r") as file:
            print("\nAccNo\tName\tBalance")
            print("-" * 30)
            for line in file:
                acc_no, name, balance = line.strip().split(",")
                print(f"{acc_no}\t{name}\t{balance}")
    except FileNotFoundError:
        print("No accounts found.")


def deposit():
    acc_no = input("Enter Account Number: ")
    amount = int(input("Enter amount to deposit: "))
    lines = []
    updated = False

    try:
        with open("accounts.txt", "r") as file:
            lines = file.readlines()

        with open("accounts.txt", "w") as file:
            for line in lines:
                a, name, balance = line.strip().split(",")
                if a == acc_no:
                    balance = str(int(balance) + amount)
                    updated = True
                file.write(f"{a},{name},{balance}\n")

        if updated:
            print("Amount deposited successfully!")
        else:
            print("Account not found.")

    except FileNotFoundError:
        print("No records available.")


def withdraw():
    acc_no = input("Enter Account Number: ")
    amount = int(input("Enter amount to withdraw: "))
    lines = []
    updated = False

    try:
        with open("accounts.txt", "r") as file:
            lines = file.readlines()

        with open("accounts.txt", "w") as file:
            for line in lines:
                a, name, balance = line.strip().split(",")
                if a == acc_no:
                    if int(balance) >= amount:
                        balance = str(int(balance) - amount)
                        updated = True
                    else:
                        print("Insufficient balance!")
                file.write(f"{a},{name},{balance}\n")

        if updated:
            print("Withdrawal successful!")
        else:
            print("Account not found.")

    except FileNotFoundError:
        print("No records available.")


def check_balance():
    acc_no = input("Enter Account Number: ")
    found = False

    try:
        with open("accounts.txt", "r") as file:
            for line in file:
                a, name, balance = line.strip().split(",")
                if a == acc_no:
                    print("Account Holder:", name)
                    print("Balance:", balance)
                    found = True
                    break
        if not found:
            print("Account not found.")

    except FileNotFoundError:
        print("No records available.")


while True:
    print("\n===== Bank Management System =====")
    print("1. Create Account")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Check Balance")
    print("5. View All Accounts")
    print("6. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        create_account()
    elif choice == "2":
        deposit()
    elif choice == "3":
        withdraw()
    elif choice == "4":
        check_balance()
    elif choice == "5":
        view_accounts()
    elif choice == "6":
        print("Thank you!")
        break
    else:
        print("Invalid choice.")
