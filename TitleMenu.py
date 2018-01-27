from cocos.menu import Menu, CENTER, MenuItem, shake, shake_back, ImageMenuItem
from cocos.director import director
from cocos.scene import Scene
from MainScene import MainScene
from Constants import Constants

class TitleMenu(Menu):

    def __init__(self, state):
        super(TitleMenu, self).__init__()

        self.state = state
        self.menu_valign = CENTER
        self.menu_halign = CENTER

        self.posX, self.posY = self.position
        self.position = self.posX, self.posY - 90

        newGameBtn = ImageMenuItem(Constants.Paths.Buttons.newGame, self.loadGame)
        quitGameBtn = ImageMenuItem(Constants.Paths.Buttons.quit, self.quitGame)
        self.scale = 2

        menu_items = [
            (newGameBtn),
            (quitGameBtn)
        ]

        self.create_menu(menu_items)

    def loadGame(self):
        mainScene = MainScene(self.state)
        director.replace(mainScene)

    def quitGame(self):
        exit()

