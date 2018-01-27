# Example human/AI player data
class Player:
    def __init__(self):
        self.resources = 0
        self.tanks = 0
        self.missiles = 0
        self.nukes = 0
        self.satellites = 0


class State:
    def __init__(self):
        self.player1 = Player()
        self.player2 = Player()
