import numpy as np

# Problem-specific parameters
NUM_CITIES = 20  # Number of cities
CITIES_COORDS = np.random.rand(NUM_CITIES, 2)  # Random city coordinates

# WOA parameters
NUM_WHALES = 30
NUM_ITERATIONS = 100
A_INIT = 2.0
A_MIN = 0.2
A_DECAY = 0.95

class Whale:
    def __init__(self, position):
        self.position = position

    def evaluate_fitness(self):
        total_distance = 0
        for i in range(NUM_CITIES - 1):
            total_distance += np.linalg.norm(CITIES_COORDS[self.position[i]] - CITIES_COORDS[self.position[i+1]])
        total_distance += np.linalg.norm(CITIES_COORDS[self.position[-1]] - CITIES_COORDS[self.position[0]])
        return total_distance

def woa_tsp():
    whales = [Whale(np.random.permutation(NUM_CITIES)) for _ in range(NUM_WHALES)]
    best_whale = min(whales, key=lambda whale: whale.evaluate_fitness())

    A = A_INIT
    for _ in range(NUM_ITERATIONS):
        for whale in whales:
            r = np.random.random()
            A *= A_DECAY

            if r < 0.5:
                # Exploration phase
                D = np.abs(A * CITIES_COORDS[best_whale.position] - CITIES_COORDS[whale.position])
                new_position = CITIES_COORDS[best_whale.position] - A * D * (2 * np.random.random() - 1)
            else:
                # Exploitation phase
                new_position = A * np.exp(-A * (np.random.random() - 0.5)) * np.cos(2 * np.pi * (np.random.random()))

            whale.position = np.argsort(new_position)

            # Ensure valid position (all cities must be unique)
            while len(set(whale.position)) < NUM_CITIES:
                whale.position = np.random.permutation(NUM_CITIES)

        best_whale = min(whales, key=lambda whale: whale.evaluate_fitness())

    return best_whale.position

# Example usage
best_path = woa_tsp()
print("Best path found by WOA:", best_path)
