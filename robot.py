from weapon import Weapon


class Robot:
    def __init__(self, robot_name):
        self.robot_name = robot_name
        self.robot_health = 100
        self.robot_weapon = Weapon("Sword", 30)

    def robo_attack(self, dinosaur):
        dinosaur.dino_health -= self.robot_weapon.attack_power
        print(f"{dinosaur.dino_name} has been attacked for a damage of {self.robot_weapon.attack_power}")

