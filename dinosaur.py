class Dinosaur:
    def __init__(self, dino_name):
        self.dino_name = dino_name
        self.dino_health = 100
        self.dino_attack_power = 10

    def dino_attack(self, robot):
        robot.robot_health -= self.dino_attack_power
        

