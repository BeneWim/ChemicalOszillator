import random
import matplotlib.pyplot as plt

import Config
from Molecule import Molecule


class Surface:
    def __init__(self, max_x, max_y, number_of_chemicals):
        self.max_x = max_x
        self.max_y = max_y

        self.molecules = list()

        self.create_chemicals(number_of_chemicals)

        self.grid = [[list() for _ in range(self.max_y)] for _ in range(self.max_x)]

        self.embed_in_grid()

        self.type_count_timeline = list()

    def create_chemicals(self, number_of_chemicals):
        self.molecules = [Molecule.create_random_molecule(self.max_x, self.max_y) for _ in range(number_of_chemicals)]

    def embed_in_grid(self):
        for molecule in self.molecules:
            self.grid[molecule.x][molecule.y].append(molecule)

    def dominant_type(self, x, y):
        molecules = list()

        # could be done more efficiently
        for deltaX in {-1, 0, 1}:
            for deltaY in {-1, 0, 1}:
                molecules += self.grid[(x + deltaX) % Config.max_x][(y + deltaY) % Config.max_y]

        types_count = Surface.count_types(molecules)

        return max(types_count, key=types_count.get)

    def react_n_times(self, times):
        for _ in range(times):
            self.random_reaction()

        self.collect_type_count()

    def random_reaction(self):
        molecule_a = random.sample(self.molecules, 1)[0]

        try:
            molecule_b = self.get_close_molecule(molecule_a)
        # some molecules don´t have neighbours
        except ValueError:
            molecule_b = molecule_a

        molecule_a.react(molecule_b)

    def get_close_molecule(self, molecule):
        delta_x = random.randint(- Config.max_reaction_distance, Config.max_reaction_distance)
        delta_y = random.randint(- Config.max_reaction_distance, Config.max_reaction_distance)

        return random.sample(self.grid[(molecule.x + delta_x) % self.max_x][(molecule.y + delta_y) % self.max_y], 1)[0]

    def collect_type_count(self):
        type_count = Surface.count_types(self.molecules)

        self.type_count_timeline.append(type_count)

    def plot_type_timeline(self):
        for molecule_types in Config.molecule_types:
            type_timeline = list(map(lambda x: x[molecule_types], self.type_count_timeline))
            plt.plot(range(len(type_timeline)), type_timeline, label=molecule_types)

        plt.legend()
        plt.show()


    @staticmethod
    def count_types(molecules):
        count = {molecule_types: 0 for molecule_types in Config.molecule_types}

        for molecule in molecules:
            count[molecule.type] += 1

        return count
