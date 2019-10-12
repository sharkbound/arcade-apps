from random import choice

from arcade import *
from arcade import color as colors

all_colors = tuple(color for color in colors.__dict__.values() if isinstance(color, tuple) and len(color) == 3)


def random_color():
    return choice(all_colors)


class Main(Window):
    def run(self):
        self.offset = 10
        self.shapes = ShapeElementList()
        self.shapes.center_x, self.shapes.center_y = self.width / 2, self.height / 2
        self.x = self.width / 2
        self.y = self.height / 2
        self.step = 1
        self.draw_lines()
        run()

    def on_key_press(self, symbol: int, modifiers: int):
        if symbol == key.Q:
            close_window()
        elif symbol == key.SPACE:
            self.shapes = ShapeElementList()
            self.draw_lines()

    def draw_lines(self):
        for _ in range(100):
            self.shapes.append(create_line(0, 0, ))

    def on_draw(self):
        self.shapes.draw()


Main().run()
