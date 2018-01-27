import cocos
import pyglet
import math
from cocos.text import Label
from cocos import scene
from cocos.layer import Layer
from cocos.director import director
from cocos.actions import *

class BackgroundLayer(Layer):
    def __init__(self):
        super(BackgroundLayer, self).__init__()
        self.skySprite = cocos.sprite.Sprite('assets/World_background_1280px.png')
        self.skySprite.position = 0, 0
        self.skySprite.image_anchor = 0, 0
        self.add(self.skySprite)

        self.groundSprite = cocos.sprite.Sprite("assets/World_foreground_1280px.png")
        self.groundSprite.position = 0, 0
        self.groundSprite.image_anchor = 0, 0
        self.add(self.groundSprite)
        pass

class HudLayer(Layer):
    def __init__(self):
        super(HudLayer, self).__init__()
        self.resourceLabel = Label(
            "RESOURCES 0/2000",
            font_name = "DejaVu Sans",
            font_size = 32,
            anchor_x = 'center',
            anchor_y = 'center'
        )

        self.resourceLabel.position = 1280 / 2, 720 - 20
        self.add(self.resourceLabel)

class MainLayer(Layer):
    is_event_handler = True

    def __init__(self):
        super(MainLayer, self).__init__()

        self.sprite = cocos.sprite.Sprite('assets/tank_green_128px.png')
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
