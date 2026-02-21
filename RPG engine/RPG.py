# Random will be used to randomize player attack and ennemy attack
import random
# Defining important variables
pla_name = input("Welome user to RPG type in your name\n")
default_inv = {
    "health_potion":1,
    "sword":1
}
PLA_HEALTH = 50
pla_dodge_prob = 0.15
current_room = 0
valid_choices = ("north","south","west","east","check stats","attack","open chest")
directions = ("north","south","west","east")

# Map of the world
world_map = {
    0:{
       "desc":"A random plain where there is nothing but a dunegon laying ahead",
       "ennemy_count":0,
       "is_chest":False,
       "exits":{"north":1}
    },
    1:{
       "desc":"you enetred the dunegon this room is empty but there is a door ahead",
       "ennemy_count":0,
       "is_chest":False,
       "exits":{"north":2,"south":0}
    },
    2:{
       "desc":"You are in the dunegon there is an ennemy ahead of you while there is a door at your left",
       "ennemy_count":1,
       "is_chest":False,
       "exits":{"east":3,"south":1}
    },
    3:{
       "desc":"This room contains a chest congrats",
       "ennemy_count":0,
       "is_chest":True,
       "exits":{"south":2}
    }

}


def show_stats(inv:dict):
    # for each item in the inv list the loop goes throw each item and prints it
    print(f"Health:{PLA_HEALTH}")
    print("--------INVENTORY--------")
    for key,value in inv.items():
        print(f"{key}: {value}")
    print("-------------------------")


def show_options():
    print("\nChoose direction (North,South,East,West)")
    print("Check stats")
    print("attack (if there is an ennemy)")
    print("open chest")


def show_room_desc(map,room):
    print(map[room]["desc"])
    if map[room]["ennemy_count"] > 0:
       print("Watch out there is an ennemy here")
    else:
        print("There is no enney here")

    if map[room]["is_chest"] == True:
        print("Amazing there is a chest in this room")


def open_chest(world_map,inv:dict,reward,cur_room):
    print(f"\nyou obtained a {reward}")
    inv[reward] = inv.get(reward,0) + 1
    world_map[cur_room]["is_chest"] = False


def atk_engine(inv,world_map,current_room):
    print("\nCombat locked")
    ennemy = [30,]
    while True:
       enm_dmg = random.randint(1,10)
       global PLA_HEALTH
       pla_dammage = random.randint(1,10)
       print("1.attack")
       print("2.use health potion")

       move = input("What do you do?(1 or 2)")

       if move == "1":
            ennemy[0] -= pla_dammage
            print(f"\nyou dealt {pla_dammage}")
            print("ennemy is attacking ...")


            # probabilty to dodge
            if random.random() < pla_dodge_prob:
                print("\nyou dodged no dammage taken")
            else:
                PLA_HEALTH -= enm_dmg
                print(f"\nyou took {enm_dmg} of dammage remaning hp {PLA_HEALTH}")


            # if player or ennely dies the attack ends
            if PLA_HEALTH <= 0:
                    print("you died")
                    input()
                    exit()
            elif ennemy[0] <= 0:
                    print("you killed the ennemy")
                    world_map[current_room]["ennemy_count"] -= 1
                    break
            
            
       elif move == "2":
            if inv["health_potion"] > 0:
                PLA_HEALTH += 20
                inv["health_potion"] -= 1
                print(f"\nNice you have {PLA_HEALTH}")
            else:
                print("\nNo potions")

       else:
        print("\nPlease type valid option 1 or 2")
       


print("The game started")
# RPG main game loop
while True:
    print(f"you are cuurently in room {current_room}")

    show_room_desc(world_map,current_room)
    show_options()
    choice = input(f"\nWhat do you do? {pla_name}\n").lower()
    
    # we check if the choice is  a valid chcoies in the first place   
    if choice in valid_choices:
        # we check if the choice is a direction
        if choice in directions:
       # if true we start here the moving process
            if world_map[current_room]["ennemy_count"] <= 0:
                if choice in world_map[current_room]["exits"]:
                    current_room = world_map[current_room]["exits"][choice]
                    show_room_desc(world_map,current_room)
                else:
                    print("You hit a wall\n")
            else:
                print("\ncant run there is an enney here")


        elif choice == "check stats":
            show_stats(default_inv)


        elif choice == "attack":
            if world_map[current_room]["ennemy_count"] > 0:
                atk_engine(default_inv,world_map,current_room,)
            else:
                print("There is no ennemy\n")
            
        elif choice == "open chest":
            if world_map[current_room]["is_chest"] == True:
                open_chest(world_map,default_inv,"health_potion",current_room)
            else:
                print("There is no chest\n")
    else:
        print("Please type a valid option\n")
    

       