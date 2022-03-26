from robot import Robot

class Fleet:
    def __init__(self):
        self.robots_list = []

    def create_fleet(self):
        robot_one = Robot("John")
        self.robots_list.append(robot_one)
        robot_two = Robot("Paul")
        self.robots_list.append(robot_two)
        robot_three = Robot("George")
        self.robots_list.append(robot_three)

    def list_avail_robots(self):
        self.create_fleet()
        # loops through the robots_list and adds one number to the index each
        # time it loops 
        index = 0
        for robot in self.robots_list:
            # robot.robot_name is referring to the robot class instance
            # variable called robot name
            # each time the loop runs it will be a different robot 
            print(f" Press {index} for {robot.robot_name}")
            index += 1
        # print("Press 0 for " + self.robots_list[0].robot_name)
        # print("Press 1 for " + self.robots_list[1].robot_name)
        # print("Press 2 for " + self.robots_list[2].robot_name)
