class Entity:
    def __init__(self,name:str,hp:int,dammage:int):
        self.hp = hp
        self.name = name
        self.dammage = dammage
    
    def take_dammage(self,dmg:int):
        try:
            self.hp -= dmg
            if self.hp < 0:
                self.hp = 0
                print(f"{self.name} died.")
                return

            print(f"Dammage taken {dmg} remaning health {self.hp}.")
        except TypeError:
            print("Invalid data.")

    def talk(self):
        print(f"I am {self.name} i have {self.hp} hp i deal {self.dammage} dammage.")


enm_dict = {
    "Slime":(20,10),
    "Zombie":(40,20),
    "Human":(60,30)
}

enm_list = []
for enm_name , enm_stats in enm_dict.items():
    enm_list.append(Entity(enm_name,enm_stats[0],enm_stats[1]))