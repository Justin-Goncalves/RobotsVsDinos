
from fleet import Fleet
from herd import Herd

class Battlefield: 
    def __init__(self):
        self.fleet = Fleet()
        self.herd = Herd()
        self.game_not_over = True

    def run_game(self):
        self.display_welcome()
        self.battle()
        

    def display_welcome(self):
        print("Welcome player to the battlefield! ")
        print()

    def battle(self):
        while self.game_not_over == True:
            self.dino_turn()
            self.robo_turn()
            if len(self.herd.herd_list) == 0:
                self.display_winner("Robots")
                self.game_not_over = False
            elif len(self.fleet.robots_list) == 0:
                self.display_winner("Dinosaurs")
                self.game_not_over = False

    def dino_turn(self):
        # I created an if statement to not call the function if there are no more dinosaurs in the herd list
        # I call to display all the dinosaur choices
        # asking the user to type a number for their chosen dinosaur
        # Using the user input from above as an index position in the herd_list
        # I call to display all the robots to choose to attack
        # asking the user to type a number for their chosen robot to attack
        # using the user input from above as an index position in the robots_list
        # the chosen dinosaur to attack the chosen robot with the info above
        # if robot is dead, remove them from the list
        if len(self.herd.herd_list) != 0:
            self.show_dino_options()
            dino_index_position = int(input("Pick a Dinosaur from above: "))
            self.show_robo_options()
            robot_index_position = int(input("Which Robot would you like to attack: "))
            dinosaur_choice = self.herd.herd_list[dino_index_position]
            robot_choice = self.fleet.robots_list[robot_index_position]
            dinosaur_choice.dino_attack(robot_choice)
            if robot_choice.robot_health <= 0:
                print(f"{dinosaur_choice.dino_name} killed {robot_choice.robot_name}! ")
                self.fleet.robots_list.remove(robot_choice)

       
        
    
    def robo_turn(self):
        #We call to display all the robot choices
        #asking the user to type a number for their chosen robot
        #Using the user input from above as an index position in the fleet_list
        # we call to display all the dinos to choose to attack
         # asking the user to type a number for their chosen dino to attack
        # using the user input from above as an index position in the dinosaur_list
        # the chosen dinosaur to attack the chosen robot with the info above
        # if the dinosaur is dead, remove him from the list
        if len(self.fleet.robots_list) != 0:
            self.show_robo_options()
            robot_index_position = int(input("Pick a Robot from above: "))
            robot_choice = self.fleet.robots_list[robot_index_position]
            self.show_dino_options()
            dino_index_position = int(input("Now choose a dinosaur you want to attack: "))
            dinosaur_choice = self.herd.herd_list[dino_index_position]
            robot_choice.robo_attack(dinosaur_choice)
            if dinosaur_choice.dino_health <= 0:
                print(f"{robot_choice.robot_name} killed {dinosaur_choice.dino_name}! ")
                self.herd.herd_list.remove(dinosaur_choice)
    




    def show_dino_options(self):
        # Print out the options for the user to choose from
        self.herd.list_avail_dinos()
            

    def show_robo_options(self):
        # print out the options for the user to choose from if it is a robot chose
        self.fleet.list_avail_robots()

    def display_winner(self,winner):
        print(f"The {winner} have won! Game Over! ")




