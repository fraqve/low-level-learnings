import logic
import os

def rerroute(choice:str,user_data:dict):
    if choice == "1":
        logic.deposit(user_data)
    elif choice == "2":
        logic.withdraw(user_data)
    elif choice == "3":
        logic.save(user_data)
        exit()

def show_opt(user_data:dict):
    while True:
        os.system("clear")
        valid_opt =("1","2","3")
        print(f"Current balance {user_data['balance']}")
        print("1.Deposit")
        print("2.WithDraw")
        print("3.Save and exit")
        choice = input("(1/2/3) ")

        #Handling the user choices
        if choice in valid_opt:
            return choice
        else:
            os.system("clear")
            print("\nPlease type a valid choice")
            input()



usr_acnt_data = logic.load()
# Main program loop
while True:
     choice = show_opt(usr_acnt_data)
     rerroute(choice,usr_acnt_data)
