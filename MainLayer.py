import cocos
import pyglet
import random
from cocos.layer import Layer
from cocos.actions import MoveBy, MoveTo, Jump
from cocos.sprite import Sprite
from cocos.director import director
from cocos.scenes import *
from Constants import Constants
from EndScene import EndScene


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

        # Update all tanks, missiles, etc in update() every frame
        self.schedule(self.update)

    def on_mouse_press(self, x, y, buttons, modifiers):
        # Maybe missile targeting here?
        pass

    def on_key_press(self, key, modifiers):
        if key == pyglet.window.key.F1:
            self.state.player1.health = 0
            self.showEndScene()
        if key == pyglet.window.key.F2:
            self.state.player2.health = 0
            self.showEndScene()

    def on_tank_purchase(self, emitter):
        print("tank purchased")
        tank = Sprite(Constants.Paths.Units.tankGreen)
        self.state.player1.tanks.append(tank)
        self.add(tank)
        tank.position = random.randint(tank.width / 2, 300), 190 + tank.height / 2
        tank.velocity = (100.0, 0.0)
        tank.gasoline = random.randint(0, 1280)

    def update(self, dt):
        for tank in self.state.player1.tanks:
            tank.position = tank.position[0] + tank.velocity[0] * dt, tank.position[1]

    def showEndScene(self):
        director.replace(ZoomTransition(EndScene(self.state)))
