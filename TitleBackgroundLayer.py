import cocos
from cocos.sprite import Sprite
from cocos.layer import Layer
from Constants import Constants


class TitleBackgroundLayer(Layer):

    def __init__(self):
        super(TitleBackgroundLayer, self).__init__()

        self.sprite = Sprite(Constants.Paths.Backgrounds.menu)
        self.sprite.position = 640, 360
        self.add(self.sprite)
