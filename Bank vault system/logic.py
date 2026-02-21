import json
import os

filename = "save.json"
default_data ={
    "balance": 100,
    "item": None
}


def save(user_data:dict={}): 
    with open(filename,"w") as f:
        json.dump(user_data,f)
        print("Save succeful")
        input()


def load():
    try:
        with open(filename,"r") as file:
            data = json.load(file)
        return data
    except:
        print(f"No save file found creating default template ...")
        with open(filename,"w") as f:
            json.dump(default_data,f)
        return default_data
    

def deposit(user_data:dict):
    while True:
        os.system("clear")
        try:
            dpt_amount = int(input("Whats the amount to deposite\n"))
            # Handling the case where user types negative number ex: -1
            if dpt_amount >= 0:
                user_data["balance"] += dpt_amount
                print(f"Succes! current balance {user_data['balance']}")
                input()
                break
            else:
                print("you cannont type a negative number")
                input()

        except ValueError:
            print("Please type in a valid number")
            input()


def withdraw(user_data:dict):
    while True:
        os.system("clear")
        try:
            wit_amount = int(input("What's amount of the withdraw\n"))

            if user_data["balance"] >= wit_amount:
                user_data["balance"] -= wit_amount
                print(f"Succes! current balance {user_data['balance']}")
                input()
                break
            else:
                print("Insufficient Funds")
                is_countinue = input("Go back? (yes/no)").lower()
                if is_countinue == "yes":
                    break
        
        except ValueError:
            print("Please type a valid number")
            input()
    