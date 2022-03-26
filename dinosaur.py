

class Dinosaur:
    def __init__(self, dino_name,attack_power):
        self.dino_name = dino_name
        self.dino_health = 100
        self.dino_attack_power = attack_power
# we don't need to further notate for the dino_attack_power
# there is no further value
# dino_attack_power is at the end
    def dino_attack(self, robot):
        robot.robot_health -= self.dino_attack_power
        print(f"{robot.robot_name} has been attacked for a damage of {self.dino_attack_power}")
        print(f"{robot.robot_name} health is at {robot.robot_health}")

