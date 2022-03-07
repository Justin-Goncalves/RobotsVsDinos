from dinosaur import Dinosaur

class Herd:
    def __init__(self):
        self.herd_list = []
        self.create_herd()

    def create_herd(self):
        dino_one = Dinosaur("Mick")
        self.herd_list.append(dino_one)
        dino_two = Dinosaur("Keith")
        self.herd_list.append(dino_two)
        dino_three = Dinosaur("Charlie")
        self.herd_list.append(dino_three)

    def list_avail_dinos(self):
        #for x in self.herd_list:
            print("Press 0 for " + self.herd_list[0].dino_name)
            print("Press 1 for " + self.herd_list[1].dino_name)
            print("Press 2 for " + self.herd_list[2].dino_name)
