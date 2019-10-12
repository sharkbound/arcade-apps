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
        self.draw_lines()
        run()

    def on_key_press(self, symbol: int, modifiers: int):
        if symbol == key.Q:
            close_window()
        elif symbol == key.SPACE:
            self.shapes = ShapeElementList()
            self.draw_lines()

    def draw_lines(self):
        self.shapes.center_x, self.shapes.center_y = self.width, 0

        for offset in range(10, 800, 5):
            self.connecting_lines(offset)

    def connecting_lines(self, offset, color=None):
        self.shapes.append(
            create_line(0, offset, -offset, offset, color or random_color()))
        self.shapes.append(
            create_line(-offset, 0, -offset, offset, color or random_color()))

    def on_draw(self):
        self.shapes.draw()
        draw_circle_filled(self.dx, self.dy, 10, colors.RED)


Main().run()
