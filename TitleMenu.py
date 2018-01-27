from cocos.menu import Menu, CENTER, MenuItem, shake, shake_back, ImageMenuItem
from cocos.director import director
from cocos.scene import Scene
from MainScene import MainScene


class TitleMenu(Menu):

    def __init__(self, state):
        super(TitleMenu, self).__init__()

        self.state = state
        self.menu_valign = CENTER
        self.menu_halign = CENTER

        menu_items = [
            (ImageMenuItem('assets/images/UI_newgame_button.png', self.loadGame)),
            (ImageMenuItem('assets/images/UI_quit_button.png', self.quitGame))
        ]

        self.create_menu(menu_items)

    def loadGame(self):
        mainScene = MainScene(self.state)
        director.replace(mainScene)

    def quitGame(self):
        exit()

