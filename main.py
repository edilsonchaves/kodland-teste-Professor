import pgzrun
import random
import Scenario
import Character

WIDTH = 1024
HEIGHT = 768
bgScenario = []
tilesObject = []
def CreateCharacter():
    
    mainObject = Actor('characters/main/character_green_idle')
    return Character.MainCharacter(mainObject)

def CreateScenario():
    #Create Sky
    for i in range(4):
        cloudObject = Actor('background/background_clouds')
        cloud = Scenario.Tile(cloudObject, i * cloudObject.width, 0)
        bgScenario.append(cloud)
    for i in range(16):
        skyObject = Actor('background/background_sky')
        sky = Scenario.Tile(skyObject, i * skyObject.width, 256)
        bgScenario.append(sky)

    #Create background
    for i in range(4):
        bgObject = Actor('background/desertbg')
        scenario = Scenario.Tile(bgObject, i * bgObject.width, 384)
        bgScenario.append(scenario)
    # create tiles
    for i in range(16):
        tileBottomObject = Actor('tiles/terrain_sand_block_bottom')
        tileUpObject = Actor('tiles/terrain_sand_block')

        bottomTileHeight = HEIGHT - tileBottomObject.height
        upTileHeight = bottomTileHeight - tileUpObject.height
                
        tileBotton = Scenario.Tile(tileBottomObject, i * tileBottomObject.width, bottomTileHeight)
        tileUp = Scenario.Tile(tileUpObject, i * tileUpObject.width, upTileHeight)

        bgScenario.append(tileBotton)
        bgScenario.append(tileUp)
        tilesObject.append(tileUp.objeto)


mainCharacter = CreateCharacter()
CreateScenario()

def DrawScenario():
    for tile in bgScenario:
        tile.objeto.left = tile.positionX
        tile.objeto.top = tile.positionY
        tile.objeto.draw()

def draw():
    screen.clear()
    DrawScenario()
    mainCharacter.objeto.draw()

def update():
    mainCharacter.ExecutePlayerMovement(tilesObject)    

def ValidMovement(key):
    return key == 97 or key == 100 or key == 119 or key == 115

def ValidJump(key):
    return key == 32

def on_key_down(key):
    if ValidMovement(key):
        mainCharacter.KeyMovementPress(key)

    if ValidJump(key):
        mainCharacter.SetPlayerSpeed(-100)

def on_key_up(key):
    if ValidMovement(key):
        mainCharacter.KeyMovementRelease(key)

pgzrun.go()