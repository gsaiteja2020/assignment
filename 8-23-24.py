acc=int(input("enter account number\n"))
pin=int(input("enter pin\n"))

if(acc==123456 and pin==1010):
    balance=50000
    choice=int(input(" enter 1 to withdraw\n enter 2 to check balance\n  "))
    if(choice==1):
        amount=int(input("enter the amount "))
        if(amount>balance):
            print("insufficient balance")
        else:
            balance-=amount
            print("transaction successfull \n balance = " +str(balance))
    elif(choice==2):
        print(balance);
    else:
        print("choose the correct option")
else:
    print("enter correct account number and pincode")