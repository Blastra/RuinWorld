import cocos
import pyglet
import random
from cocos.layer import Layer
from cocos.actions import MoveBy, MoveTo, Jump
from cocos.sprite import Sprite
from Constants import Constants


class MainLayer(Layer):
    is_event_handler = True

    def __init__(self, state):
        super(MainLayer, self).__init__()

        self.state = state

        # Add cities first (they're in the background)
        for city in self.state.player1.cities:
            self.add(city)

        for city in self.state.player2.cities:
            self.add(city)

        self.sprite = cocos.sprite.Sprite('assets/images/tank_green_128px.png')
        self.sprite.position = 100, 100
        self.add(self.sprite)

        self.timer = 0
        self.sprite.schedule(self.scaleAll)

    def scaleAll(self, delta):
        self.timer += 1

    def on_mouse_press(self, x, y, buttons, modifiers):
        actions = MoveTo((x,y), 1) + Jump(25, 20, 3, 3)
        #self.sprite.do(MoveTo((x,y), 2) + Jump(50, 0, 1, 1))
        self.sprite.do(actions)

    def on_key_press(self, key, modifiers):
        if key == pyglet.window.key.LEFT:
            self.sprite.do(MoveBy((-50, 0), .5))
        if key == pyglet.window.key.RIGHT:
            self.sprite.do(MoveBy((50, 0), .5))
        if key == pyglet.window.key.UP:
            self.sprite.do(MoveBy((0, 50), .5))
        if key == pyglet.window.key.DOWN:
            self.sprite.do(MoveBy((0, -50), .5))

    def on_tank_purchase(self, emitter):
        print("tank purchased")
        print(self.state.player1.tanks)
        tank = Sprite(Constants.Paths.Units.tankGreen)
        self.state.player1.tanks.append(tank)
        self.add(tank)
        tank.position = random.randint(tank.width / 2, 300), 190 + tank.height / 2