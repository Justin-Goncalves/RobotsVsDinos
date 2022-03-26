from dinosaur import Dinosaur

class Herd:
    def __init__(self):
        self.herd_list = []
        

    def create_herd(self):
        dino_one = Dinosaur("Mick", 20)
        self.herd_list.append(dino_one)
        dino_two = Dinosaur("Keith", 40)
        self.herd_list.append(dino_two)
        dino_three = Dinosaur("Charlie", 30)
        self.herd_list.append(dino_three)

    def list_avail_dinos(self):
        self.create_herd()
        index = 0
        for dinosaur in self.herd_list:
            print(f"Press {index} for {dinosaur.dino_name}. ")
            index += 1
        # print("Press 0 for " + self.herd_list[0].dino_name)
        # print("Press 1 for " + self.herd_list[1].dino_name)
        # print("Press 2 for " + self.herd_list[2].dino_name)
