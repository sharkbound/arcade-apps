from arcade import *
import arcade as a


class MouseTracker(View):
    def __init__(self):
        super().__init__()
        self.mouse_pos = 0, 0
        self.shapes = ShapeElementList()

    def setup(self):
        self.shapes.center_x, self.shapes.center_y = 300, 300
        self.shapes.append(create_line(0, 0, 500, 100, color.RED))
        return self

    def on_key_press(self, symbol: int, modifiers: int):
        if (symbol == key.Q):
            close_window()

    def on_mouse_motion(self, x: float, y: float, dx: float, dy: float):
        self.mouse_pos = x, y
        self.shapes.center_x = x
        self.shapes.center_y = y

    def update(self, delta_time: float):
        self.shapes.angle = 140

    def on_draw(self):
        start_render()
        self.shapes.draw()


Window().show_view(MouseTracker().setup())
run()
