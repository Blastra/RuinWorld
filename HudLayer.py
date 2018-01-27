import pyglet
from cocos.layer import Layer
from cocos.text import Label
from cocos.sprite import Sprite
from Constants import Constants


class HudLayer(Layer, pyglet.event.EventDispatcher):
    is_event_handler = True

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

        left = 1280 / 2 - 128 / 2 - 20 - 128 / 2
        self.tankButton = Sprite(Constants.Paths.Buttons.tank)
        self.tankButton.position = left, 80
        self.add(self.tankButton)

        left += self.tankButton.width + 20

        self.missileButton = Sprite(Constants.Paths.Buttons.missile)
        self.missileButton.position = left, 80
        self.add(self.missileButton)

        left += self.missileButton.width + 20

        self.nukeButton = Sprite(Constants.Paths.Buttons.nuke)
        self.nukeButton.position = left, 80
        self.add(self.nukeButton)

    def on_mouse_motion(self, x, y, dx, dy):
        if self.tankButton.get_rect().contains(x, y):
            self.tankButton.scale = 1.1
        else:
            self.tankButton.scale = 1.0

        if self.missileButton.get_rect().contains(x, y):
            self.missileButton.scale = 1.1
        else:
            self.missileButton.scale = 1.0

        if self.nukeButton.get_rect().contains(x, y):
            self.nukeButton.scale = 1.1
        else:
            self.nukeButton.scale = 1.0

    def on_mouse_press(self, x, y, buttons, modifiers):
        if self.tankButton.get_rect().contains(x, y):
            self.tankButton.scale = 2
            self.dispatch_event('on_tank_purchase', self)


HudLayer.register_event_type('on_tank_purchase')
HudLayer.register_event_type('on_missile_purchase')
HudLayer.register_event_type('on_nuke_purchase')
