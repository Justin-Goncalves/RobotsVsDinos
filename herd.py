from dinosaur import Dinosaur

class Herd:
    def __init__(self):
        self.herd_list = [Dinosaur("Mick", 20),Dinosaur("Keith", 40), Dinosaur("Charlie", 30)]
        

    def list_avail_dinos(self):
        # for loop that loops through the appened herd_list 
        # and adds a index number every time it runs
        index = 0
        for dinosaur in self.herd_list:
            print(f"Press {index} for {dinosaur.dino_name}, Health: {dinosaur.dino_health}. ")
            index += 1
        
