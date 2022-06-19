import Config
from Surface import Surface
from Visualiser import Visualiser


def init_simulation():
    surface = Surface(Config.max_x, Config.max_y, Config.number_of_chemicals)

    visualizer = Visualiser(Config.pixel_size, surface)

    visualizer.main_screen.after(0, run_simulation(surface, visualizer))
    visualizer.main_screen.mainloop()


def run_simulation(surface, visualizer):
    surface.react_n_times(Config.number_of_reactions)

    visualizer.print_current_state()

    surface.plot_type_timeline()

    visualizer.main_screen.after(0, run_simulation(surface, visualizer))


if __name__ == '__main__':
    init_simulation()
