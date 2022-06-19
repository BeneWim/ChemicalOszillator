number_of_iterations = 10

number_of_chemicals = 6000

max_x = 100
max_y = 100

# type should be enum!!!!!!
molecule_types = {'A', 'B', 'C'}
start_molecules = {'A'}

number_of_reactions = 10000

max_reaction_distance = 2

# functionsplotter für sinusfunktionen bauen?

# reaction_rules = {'AB': (0.15, 'BB'), 'A': (0.1, 'B'), 'B': (0.1, 'C'), 'CB': (0.15, 'CC'), 'C': (0.2, 'A')}

# Periodisch
reaction_rules = {'A': (0.0003, 'B'), 'AB': (1, 'BB'),
                  'B': (0.0003, 'C'), 'BC': (1, 'CC'),
                  'C': (0.0003, 'A'), 'CA': (1, 'AA')}

pixel_size = 10

type_color = {'A': 'blue', 'B': 'orange', 'C': 'green'}

