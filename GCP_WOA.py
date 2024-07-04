import random
import numpy as np

def calculate_fitness(graph, colors):
    conflicts = 0
    for i in range(len(graph)):
        for j in range(i + 1, len(graph)):
            if graph[i][j] and colors[i] == colors[j]:
                conflicts += 1
    return conflicts

def initialize_population(num_nodes, num_colors, population_size):
    return [[random.randint(1, num_colors) for _ in range(num_nodes)] for _ in range(population_size)]

def woa_search(graph, num_colors, population_size, max_iterations):
    population = initialize_population(len(graph), num_colors, population_size)
    best_solution = None
    best_fitness = float('inf')

    for iteration in range(max_iterations):
        for i in range(population_size):
            fitness = calculate_fitness(graph, population[i])

            if fitness < best_fitness:
                best_fitness = fitness
                best_solution = population[i].copy()

        a = 2 - 2 * iteration / max_iterations  # Parameter a decreases linearly from 2 to 0

        for i in range(population_size):
            r1 = random.random()  # Random number in [0, 1)
            r2 = random.random()  # Random number in [0, 1)

            A = 2 * a * r1 - a  # Parameter A
            C = 2 * r2          # Parameter C

            # Update position
            for j in range(len(population[i])):
                D = abs(C * best_solution[j] - population[i][j])  # Distance to the best solution
                population[i][j] = best_solution[j] - A * D

                # Boundary check
                if population[i][j] < 1:
                    population[i][j] = 1
                elif population[i][j] > num_colors:
                    population[i][j] = num_colors

    return best_solution

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
    population_size = 10
    max_iterations = 100

    best_solution = woa_search(graph, num_colors, population_size, max_iterations)
    print("Best solution found:", best_solution)
