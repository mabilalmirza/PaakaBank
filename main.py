print("Welcome to Paaka Bank.")

option = ''
balance = 0
while option != 'Q':
    print("======================================")
    print("O. Open Account")
    print("D. Deposit")
    print("W. Withdrawal")
    print("Q. Quit")
    print("======================================")
    option = input("Please select Option : ")

    if option == "D":
        amount = input("Please enter deposit amount : ")
        balance += int(amount)
        print(f'Your current balance is : {balance}')
    elif option == "W":
        amount = input("Please enter withdrawal amount : ")
        balance -= int(amount)
        print(f'Your current balance is : {balance}')
    elif option == "Q":
        print("Good Bye")
    else:
        print("!!!! WRONG CHOICE !!!!")






