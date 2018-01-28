from cocos.sprite import Sprite
from cocos.scene import Scene
from Constants import Constants


class EndScene(Scene):
    def __init__(self, state):
        super(EndScene, self).__init__()
        self.state = state
        self.showEndBasedOnResult()

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
        self.add(background)

        pass