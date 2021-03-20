print("Welcome to Paaka Bank.")

option = ''
balance = 0
while option != 'X':
    print("======================================")
    print("O. Open Account")
    print("D. Deposit")
    print("W. Withdrawal")
    print("X. Exit")
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
    elif option == "X":
        print("Good Bye")
    else:
        print("!!!! WRONG CHOICE !!!!")






