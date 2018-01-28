import pyglet
from cocos.layer import Layer
from cocos.text import Label
from cocos.director import director
from cocos.scenes import *
from cocos.sprite import Sprite
from Constants import Constants
from State import State
import TitleScene

class EndLayer(Layer):
    is_event_handler = True

    def __init__(self, state):
        super(EndLayer, self).__init__()

        self.state = state
        self.showEndBasedOnResult()
        self.titleScene = TitleScene.TitleScene


    def showEndBasedOnResult(self):
        player1Health = self.state.player1.health
        player2Health = self.state.player2.health
        backgroundName = Constants.Paths.Screens.victory

        if(player1Health > player2Health):
            print("PLAYER 1 WINS")
            backgroundName = Constants.Paths.Screens.victory
        elif(player2Health > player1Health):
            print("PLAYER 2 WINS")
            backgroundName = Constants.Paths.Screens.defeat
        else:
            print("DRAW")

        background = Sprite(backgroundName)
        background.position = 1280/2, 720/2

        backToMenuLabel = Label("PRESS SPACE TO GO BACK TO MAIN MENU")
        backToMenuLabel.position = 1280/2 - 180, 720/2

        self.add(background)
        self.add(backToMenuLabel)

    def loadTitleScene(self):
        director.replace(ZoomTransition(self.titleScene(State())))

    def on_key_press(self, key, modifiers):
        if key == pyglet.window.key.SPACE:
            self.loadTitleScene()