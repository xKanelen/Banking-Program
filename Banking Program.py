# Banking Program
def show_balance(balance):
    print("-------------------------------")
    print(f"Your balance is ${balance:.2f}")
    print("-------------------------------")

def deposit():
    print("---------------------------")
    amount = float(input("Enter an amount to deposit: "))
    print("---------------------------")
    if amount < 0:
        print("----------------------------------------")
        print("Sorry, you can't deposit negative amount")
        print("----------------------------------------")
        return 0
    else:
        print(f"You deposited ${amount:.2f}")
        return amount

def withdraw(balance):
    print("------------------------------")
    to_withdraw = float(input("Enter an amount to withdraw: "))
    print("------------------------------")
    if to_withdraw > balance:
        print(f"Your balance is {balance:.2f}")
        print("Sorry, you can't withdraw less than balance")
        return 0
    elif to_withdraw < 0:
        print("-----------------------------------------")
        print("Sorry, you can't withdraw negative amount")
        print("-----------------------------------------")
    else:
        print(f"You withdrew ${to_withdraw:.2f}")
        return to_withdraw

def main():
    menu = 1
    balance = 0
    is_running = True

    while is_running:

        if menu == 1:
            print("---------------")
            print("Banking Program")
            print("1.Show Balance")
            print("2.Deposit")
            print("3.Withdraw")
            print("4.Exit")
            print("---------------")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            show_balance(balance)
            back = input("Want to go back to menu (y/n): ").lower()
            if back == "n":
                is_running = False
            elif back != "y" and back != "n":
                print("---------------")
                print("Wrong choice, back to menu")
        elif choice == "2":
            balance += deposit()
            back = input("Want to go back to menu (y/n): ").lower()
            if back =="n":
                is_running = False
            elif back != "y" and back != "n":
                print("---------------")
                print("Wrong choice, back to menu")
        elif choice == "3":
            balance -= withdraw(balance)
            back = input("Want to go back to menu (y/n): ").lower()
            if back == "n":
                is_running = False
            elif back != "y" and back != "n":
                print("----------------")
                print("Wrong choice, back to menu")
        elif choice == "4":
            is_running = False
        else:
            print("That is not a valid choice")
            print("--------------------------")

    print("Thank you! Have a nice day!")

if __name__ == '__main__':
    main()
