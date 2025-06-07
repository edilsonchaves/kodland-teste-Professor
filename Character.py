class MainCharacter:
    def __init__(self):
        self = self

    def __init__(self, objeto):
        self.objeto = objeto
        self.movement = [0,0]
        self.movementKey = [0,0]
        self.speed = 0

    def KeyMovementPress(self, key):
        match key:
            case 97:
                self.movement[0] = -5
                self.movementKey[0] = key
            case 100:
                self.movement[0] = +5
                self.movementKey[0] = key            
            case 119:
                self.movement[1] = -5
                self.movementKey[1] = key
            case 115:
                self.movement[1] = +5
                self.movementKey[1] = key

    def KeyMovementRelease(self, key):
        match key:
            case 97 | 100:
                if(key == self.movementKey[0]):
                    self.movement[0] = 0
            case 119 | 115:
                if(key == self.movementKey[1]):
                    self.movement[1] = 0

    def SetPlayerSpeed(self, speed):
        self.speed += speed
        self.objeto.y += speed

    def ExecutePlayerMovement(self, tilesObject):
        self.objeto.x += self.movement[0]
        print(self.objeto.collidelist(tilesObject))
        if self.objeto.collidelist(tilesObject) == -1:
            self.SetPlayerSpeed(3)
