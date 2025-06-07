class Scenario:
    def __init__(self,scenario):
        self.scenario = scenario

    def AddTile(self, tile):
        self.scenario.append(tile)

class Tile:
    def __init__(self, objeto, positionX, positionY):
        self.objeto = objeto
        self.positionX = positionX
        self.positionY = positionY

    def apresentar(self):
        print("Olá, meu nome é", self.objeto, "e eu tenho", self.positionX, "anos.")