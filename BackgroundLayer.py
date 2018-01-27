import cocos
from cocos.layer import Layer

class BackgroundLayer(Layer):
    def __init__(self):
        super(BackgroundLayer, self).__init__()
        self.skySprite = cocos.sprite.Sprite('assets/World_background_1280px.png')
        self.skySprite.position = 0, 0
        self.skySprite.image_anchor = 0, 0
        self.add(self.skySprite)

        self.groundSprite = cocos.sprite.Sprite("assets/World_foreground_1280px.png")
        self.groundSprite.position = 0, 0
        self.groundSprite.image_anchor = 0, 0
        self.add(self.groundSprite)
        pass