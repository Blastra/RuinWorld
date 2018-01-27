from cocos.director import director
from MainScene import MainScene
from State import State

class Game:
    def __init__(self):
        self.state = State()
        self.mainScene = MainScene(self.state)

director.init(1280, 720, caption="Ruin World")
director.run(Game().mainScene)
