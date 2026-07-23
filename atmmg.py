print("welcome to atm management system")
correctpin = 1234
balanced= 4000
pin=input("enter the pin:")
if pin == correctpin :
     print ("login")

print( "1.select the lanuage")    
print("2.check the balance")       
print("3.withdraw the money")
choice = input ("enter your choice 1/2/3 :")
if choice == "1":

    language = input("Select hindi/english: ")

    if language == "hindi":
        print("Hindi selected")

    elif language == "english":
        print("English selected")

    else:
        print("Invalid")

elif choice == "2":

    print(f"Your balance is {balanced}" )
elif choice == "3":

    money = int(input("Enter withdraw amount: "))

    if money <= balanced:
        balanced = balanced - money
        print("Withdraw successfully")
        print("Remaining balance:", balanced)

    else:
        print("Insufficient balance")





  




