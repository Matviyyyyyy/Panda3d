from direct.showbase.ShowBase import ShowBase

import Mapmaneger


class Game(ShowBase):
    def __init__(self):
        super().__init__(self)

        land = Mapmaneger.Mapmanager()
game = Game()
game.run()
