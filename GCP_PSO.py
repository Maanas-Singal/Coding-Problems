import random
import numpy as np

class Particle:
    def __init__(self, num_nodes, num_colors):
        self.position = [random.randint(1, num_colors) for _ in range(num_nodes)]
        self.velocity = [0] * num_nodes
        self.best_position = self.position.copy()
        self.fitness = float('inf')

def calculate_fitness(graph, colors):
    conflicts = 0
    for i in range(len(graph)):
        for j in range(i + 1, len(graph)):
            if graph[i][j] and colors[i] == colors[j]:
                conflicts += 1
    return conflicts

def update_particle_velocity(particle, global_best_position, w, c1, c2):
    for i in range(len(particle.position)):
        particle.velocity[i] = w * particle.velocity[i] + \
                               c1 * random.random() * (particle.best_position[i] - particle.position[i]) + \
                               c2 * random.random() * (global_best_position[i] - particle.position[i])

def update_particle_position(particle, num_colors):
    for i in range(len(particle.position)):
        new_position = int(round(particle.position[i] + particle.velocity[i]))
        particle.position[i] = max(1, min(num_colors, new_position))  # Ensure within bounds

def graph_coloring_pso(graph, num_colors, num_particles, max_iterations, w=0.5, c1=1.5, c2=1.5):
    num_nodes = len(graph)
    particles = [Particle(num_nodes, num_colors) for _ in range(num_particles)]
    global_best_position = None
    global_best_fitness = float('inf')

    for _ in range(max_iterations):
        for particle in particles:
            particle.fitness = calculate_fitness(graph, particle.position)

            if particle.fitness < calculate_fitness(graph, particle.best_position):
                particle.best_position = particle.position.copy()

            if particle.fitness < global_best_fitness:
                global_best_fitness = particle.fitness
                global_best_position = particle.position.copy()

        for particle in particles:
            update_particle_velocity(particle, global_best_position, w, c1, c2)
            update_particle_position(particle, num_colors)

    return global_best_position

# Example usage:
if __name__ == "__main__":
    # Example graph adjacency matrix (undirected):
    graph = [
        [0, 1, 0, 1],
        [1, 0, 1, 0],
        [0, 1, 0, 1],
        [1, 0, 1, 0]
    ]
    num_nodes = len(graph)
    num_colors = 3
    num_particles = 10
    max_iterations = 100

    best_solution = graph_coloring_pso(graph, num_colors, num_particles, max_iterations)
    print("Best solution found:", best_solution)
