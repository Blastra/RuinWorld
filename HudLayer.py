from cocos.layer import Layer
from cocos.text import Label

class HudLayer(Layer):
    def __init__(self, state):
        super(HudLayer, self).__init__()

        self.state = state

        self.resourceLabel = Label(
            "RESOURCES 0/2000",
            font_name = "DejaVu Sans",
            font_size = 32,
            anchor_x = 'center',
            anchor_y = 'center'
        )

        self.resourceLabel.position = 1280 / 2, 720 - 20
        self.add(self.resourceLabel)
