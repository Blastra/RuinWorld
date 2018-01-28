from cocos.director import director
from State import State
from TitleScene import TitleScene


class Game:
    def __init__(self):
        self.state = State()
        self.titleScene = TitleScene(self.state)


director.init(width=1280, height=720, do_not_scale=True, caption="Ruin World")
director.run(Game().titleScene)
