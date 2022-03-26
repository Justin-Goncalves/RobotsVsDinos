from robot import Robot

class Fleet:
    def __init__(self):
        self.robots_list = [Robot("John"),Robot("Paul"),Robot("George")]

    def list_avail_robots(self):
        # loops through the robots_list and adds one number to the index each
        # time it loops 
        index = 0
        for robot in self.robots_list:
            # robot.robot_name is referring to the robot class instance
            # variable called robot name
            # each time the loop runs it will be a different robot 
            print(f" Press {index} for {robot.robot_name}, Health: {robot.robot_health}")
            index += 1

