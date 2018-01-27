import pyglet # ..may be needed for some audio stuff
import cocos
import cocos.audio.pygame.mixer
import cocos.audio.pygame.music

from BackgroundLayer import BackgroundLayer
from MainLayer import MainLayer
from HudLayer import HudLayer
from cocos.scene import Scene
from State import State
from Constants import Constants


class MainScene(Scene):
    def __init__(self, state):
        super(MainScene, self).__init__()

        self.state = State()

        self.add(BackgroundLayer(self.state))
        self.add(MainLayer(self.state))
        self.add(HudLayer(self.state))

        # This way does not work for some reason:
        #cocos.audio.pygame.music.load("assets/musics/33pTransition.wav")
        #self.load_music('assets/musics/NukeRumble.ogg')
        #self.play_music()

        # Requires avbin dependency (may be difficult on Windows/Linux):
        cocos.audio.pygame.mixer.init()
        music = cocos.audio.pygame.music.load(Constants.musicPaths[0])
        cocos.audio.pygame.music.play()
