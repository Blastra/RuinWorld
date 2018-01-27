import cocos
from cocos.sprite import Sprite
from cocos.layer import Layer

class TitleBackgroundLayer(Layer):

    def __init__(self):
        super(TitleBackgroundLayer, self).__init__()

        self.sprite = Sprite('assets/images/UI_menu_background.png')
        self.sprite.position = 640, 360
        self.add(self.sprite)
