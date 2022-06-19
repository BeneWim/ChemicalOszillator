import math
import random

import Config


class Molecule:
    def __init__(self, x, y, molecule_type):
        self.x = x
        self.y = y
        self.type = molecule_type

    def react(self, molecule):
        if self == molecule:
            self.self_react()
            return

        try:
            reaction_likelyhood, reaction_results = Config.reaction_rules[self.type + molecule.type]

        # Rule is not defined
        except KeyError:
            return

        if random.random() < reaction_likelyhood:
            self.type = reaction_results[0]
            molecule.type = reaction_results[1]

    def self_react(self):
        try:
            reaction_likelihood, reaction_results = Config.reaction_rules[self.type]

        # Rule is not defined
        except KeyError:
            return

        if random.random() < reaction_likelihood:
            self.type = reaction_results

    @classmethod
    def create_random_molecule(cls, max_x, max_y):
        x = random.randint(0, max_x - 1)
        y = random.randint(0, max_y - 1)

        molecule_type = random.sample(Config.start_molecules, 1)[0]

        return Molecule(x, y, molecule_type)
