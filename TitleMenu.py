from cocos.menu import Menu, CENTER, MenuItem, shake, shake_back, ImageMenuItem

class TitleMenu(Menu):
    def __init__(self):
        super(TitleMenu, self).__init__()
        self.menu_valign = CENTER
        self.menu_halign = CENTER

        menu_items = [
            (ImageMenuItem('assets/images/UI_newgame_button.png', self.loadGame)),
            (ImageMenuItem('assets/images/UI_quit_button.png', self.quitGame))
        ]

        self.create_menu(menu_items)

    def loadGame(self):
        # Load game scene
        pass


    def quitGame(self):
        exit()

