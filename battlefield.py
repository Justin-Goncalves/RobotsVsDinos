
from fleet import Fleet
from herd import Herd

class Battlefield: 
    def __init__(self):
        self.fleet = Fleet()
        self.herd = Herd()
        self.chosen_dino_index = 0
        self.chosen_robo_index = 0

    def run_game(self):
        self.display_welcome()
        self.battle()
        

    def display_welcome(self):
        print("Welcome player to the battlefield")
        self.herd.list_avail_dinos()
        self.chosen_dino_index = input("Choose a dinosaur: ")
        self.fleet.list_avail_robots()
        self.chosen_robo_index = input("Choose a robot: ")
    
    def battle(self):
        while self.fleet.fleet_list != [] and self.herd.herd_list != []:
            self.show_dino_opponent_options()
            self.show_robo_opponent_options()
            self.dino_turn(self.chosen_dino_index)
            self.robo_turn(self.chosen_robo_index)

    def dino_turn(self,dinosaur_index):
        self.herd.herd_list[dinosaur_index].dino_attack(self.fleet.fleet_list[self.chosen_robo_index])
        if self.fleet.fleet_list[self.chosen_robo_index].health == 0:
            self.fleet.fleet_list.pop(self.chosen_robo_index)
    
    def robo_turn(self, robot_index):
        #Fleet()[].dinosaur.dino_health -= self.robot_weapon(Herd()[0])
        self.fleet.fleet_list[robot_index].robo_attack(self.herd.herd_list[self.chosen_dino_index])
        if self.herd.herd_list[self.chosen_dino_index].health == 0:
            self.herd.herd_list.pop(self.chosen_dino_index)

    def show_dino_opponent_options(self):
        # Print out the options for the user to choose from
        print("Dinosaur's Turn To Attack ")
        dino_attack = input("Press 0 to attack: ")
        if dino_attack == "0":
            print("Dinosaur hits Robot ")
        else:
            print("Invalid entry. Press 0 to attack ")
            

    def show_robo_opponent_options(self):
        print("Robot's Turn To Attack ")
        robo_attack = input("Press 1 to attack: ")
        if robo_attack == "1":
            print("Robot hits Dinosaur ")
        else: 
            print("Invalid entry. Press 1 to attack: ")

    def display_winners(self):
        if self.robot_health == 0:
            print("Dinosaur is the winner! ")
        elif self.dino_health == 0:
            print("Robot is the winner! ")
