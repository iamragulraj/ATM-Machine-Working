print("Please insert the card....!\nChoose Yes or No")
n=input()
a = "Withdraw the Amount"
b = "Deposit the Amount"
c = "Change the pin"
d = "Check Balance"
if n==("Yes"):
    m=int(input("Enter the pin number:"))
    print("Select one of the  Following Details\na = Withdraw the Amount\nb = Deposit the Amount\nc = Change the pin\nd = Check Balance")
    e=input()
    if e=="a":
        A=int(input("Enter the Withdrawal Amount:"))
        print("Please Collect your money")
    if e == "b":
        B= int(input("Enter the Amount:"))
        print("Your money has been deposited successfully")
    if e == "c":
        C = int(input("Enter the new pin:"))
        print("Your pin has been changed successfully")
    if e == "d":
        print("Your balance is 10000000")
    print("Thank you for the Transaction...!")
else:
    print("Transaction has been cancelled...!")