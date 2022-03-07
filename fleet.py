from robot import Robot

class Fleet:
    def __init__(self):
        self.fleet_list = []
        self.create_fleet()

    def create_fleet(self):
        robot_one = Robot("John")
        self.fleet_list.append(robot_one)
        robot_two = Robot("Paul")
        self.fleet_list.append(robot_two)
        robot_three = Robot("George")
        self.fleet_list.append(robot_three)

    def list_avail_robots(self):
                #for x in self.herd_list:
        print("Press 0 for " + self.fleet_list[0].robot_name)
        print("Press 1 for " + self.fleet_list[1].robot_name)
        print("Press 2 for " + self.fleet_list[2].robot_name)