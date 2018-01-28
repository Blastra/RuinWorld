import cocos
from Constants import Constants
from cocos.sprite import Sprite


class Movable(Sprite):
    def __init__(self):
        super(Movable, self).__init__()
        self.velocity = (0, 0)


class Player:
    def __init__(self):
        self.resources = 0
        self.tanks = []
        self.missiles = []
        self.nukes = []
        self.satellites = 0
        self.cities = []


class State:
    def __init__(self):
        self.player1 = Player() # Human player
        self.player2 = Player() # AI player

        city1 = cocos.sprite.Sprite(Constants.Paths.Units.city)
        city1.position = (0 + city1.width / 2, 190 + city1.height / 2)
        self.player1.cities.append(city1)

        city2 = Sprite(Constants.Paths.Units.city)
        city2.position = (1280 - city2.width / 2, 190 + city2.height / 2)
        city2.scale_x = -1.0
        self.player2.cities.append(city2)

