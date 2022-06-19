from tkinter import *

import Config


class Visualiser:
    def __init__(self, resolution_size, surface):
        self.surface = surface
        self.resolution_size = resolution_size

        width = surface.max_x * resolution_size
        height = surface.max_y * resolution_size

        self.main_screen = Tk()

        self.canvas = Canvas(self.main_screen, width=width, height=height)

    def print_current_state(self):
        self.canvas.delete('all')

        for x in range(self.surface.max_x):
            for y in range(self.surface.max_y):
                dominant_type = self.surface.dominant_type(x, y)

                dominant_color = Config.type_color[dominant_type]

                self.canvas.create_rectangle(x * self.resolution_size, y * self.resolution_size,
                                             (x + 1) * self.resolution_size, (y + 1) * self.resolution_size
                                             , fill=dominant_color, outline=dominant_color)

        self.canvas.pack()
        self.main_screen.update()

