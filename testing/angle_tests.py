from collections import namedtuple
from math import cos, sin, radians

from arcade import *

Pos = namedtuple('Pos', 'x y')


class Main(Window):
    def setup(self):
        self.x = self.y = 0
        self.angle = 0
        self.shapes = ShapeElementList()
        self.populate()
        self.p = Pos(1, 2)
        return self

    def populate(self):
        cx, cy = self.width / 2, self.height / 2
        DIST = 10
        for offset in range(1, 360):
            self.shapes.append(
                create_ellipse_filled(cx + (cx * cos(radians(offset)) + DIST), cy + (cy * sin(radians(offset)) + DIST),
                                      10, 10,
                                      color.RED))

    def on_key_press(self, symbol: int, modifiers: int):
        if symbol == key.Q:
            close_window()

    def on_draw(self):
        self.shapes.draw()

    def run(self):
        self.setup()
        run()


Main().run()
