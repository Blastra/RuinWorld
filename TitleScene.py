from cocos.sprite import Sprite
from cocos.scene import Scene
from cocos.layer import Layer
from cocos.director import director
from TitleBackgroundLayer import TitleBackgroundLayer
from TitleMenu import TitleMenu


class TitleScene(Scene):
    is_event_handler = True

    def __init__(self, state):
        super(TitleScene, self).__init__()

        self.state = state

        self.add(TitleBackgroundLayer())
        self.add(TitleMenu(self.state))
