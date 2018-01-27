import cocos
from cocos.director import director
from HudLayer import HudLayer
from MainLayer import MainLayer
from BackgroundLayer import BackgroundLayer

# MAIN STUFF:

class MainScene(cocos.scene.Scene):
    def __init__(self):
        super(MainScene, self).__init__()
        pass

        self.add(BackgroundLayer())
        self.add(MainLayer())
        self.add(HudLayer())
        #cocos.audio.pygame.music.load("assets/musics/33pTransition.wav")
        self.load_music('assets/musics/NukeRumble.ogg')
        self.play_music()

director.init(1280, 720, caption="Ruin World")
director.run(MainScene())

#director.run(
#    scene.Scene(
#        BackgroundLayer(),
#        MainLayer(),
#        HudLayer()
#    )
#)
