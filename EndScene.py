from cocos.scene import Scene
from EndLayer import EndLayer

class EndScene(Scene):

    def __init__(self, state):
        super(EndScene, self).__init__()

        self.state = state
        endLayer = EndLayer(self.state)

        self.add(endLayer)
