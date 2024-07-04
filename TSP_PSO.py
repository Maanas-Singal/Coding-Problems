import numpy as np

# Problem-specific parameters
NUM_CITIES = 20  # Number of cities
CITIES_COORDS = np.random.rand(NUM_CITIES, 2)  # Random city coordinates

# PSO parameters
NUM_PARTICLES = 30
NUM_ITERATIONS = 100
INERTIA_WEIGHT = 0.7
C1 = 1.5
C2 = 1.5

class Particle:
    def __init__(self, position):
        self.position = position
        self.velocity = np.zeros_like(position)
        self.best_position = position.copy()
        self.best_fitness = float('inf')

    def evaluate_fitness(self):
        total_distance = 0
        for i in range(NUM_CITIES - 1):
            total_distance += np.linalg.norm(CITIES_COORDS[self.position[i]] - CITIES_COORDS[self.position[i+1]])
        total_distance += np.linalg.norm(CITIES_COORDS[self.position[-1]] - CITIES_COORDS[self.position[0]])
        return total_distance

def pso_tsp():
    particles = [Particle(np.random.permutation(NUM_CITIES)) for _ in range(NUM_PARTICLES)]
    global_best_position = None
    global_best_fitness = float('inf')

    for _ in range(NUM_ITERATIONS):
        for particle in particles:
            fitness = particle.evaluate_fitness()
            if fitness < particle.best_fitness:
                particle.best_fitness = fitness
                particle.best_position = particle.position.copy()

            if fitness < global_best_fitness:
                global_best_fitness = fitness
                global_best_position = particle.position.copy()

            # Update velocity
            particle.velocity = (INERTIA_WEIGHT * particle.velocity +
                                 C1 * np.random.rand() * (particle.best_position - particle.position) +
                                 C2 * np.random.rand() * (global_best_position - particle.position))

            # Update position
            particle.position = np.argsort(particle.position + particle.velocity)

    return global_best_position

# Example usage
best_path = pso_tsp()
print("Best path found by PSO:", best_path)
