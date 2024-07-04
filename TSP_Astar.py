import numpy as np
import heapq

# Problem-specific parameters
NUM_CITIES = 20  # Number of cities
CITIES_COORDS = np.random.rand(NUM_CITIES, 2)  # Random city coordinates

def calculate_total_distance(path):
    total_distance = 0
    for i in range(NUM_CITIES - 1):
        total_distance += np.linalg.norm(CITIES_COORDS[path[i]] - CITIES_COORDS[path[i+1]])
    total_distance += np.linalg.norm(CITIES_COORDS[path[-1]] - CITIES_COORDS[path[0]])
    return total_distance

def a_star_tsp():
    start_node = (0, tuple([0]))  # (cost, path)
    priority_queue = [start_node]
    best_path = None

    while priority_queue:
        cost, path = heapq.heappop(priority_queue)

        if len(path) == NUM_CITIES:
            path_cost = calculate_total_distance(path)
            if best_path is None or path_cost < calculate_total_distance(best_path):
                best_path = path
        else:
            last_city = path[-1]
            for city in range(NUM_CITIES):
                if city not in path:
                    new_path = path + (city,)
                    new_cost = calculate_total_distance(new_path)
                    heapq.heappush(priority_queue, (new_cost, new_path))

    return best_path

# Example usage
best_path = a_star_tsp()
print("Best path found by A*:", best_path)
