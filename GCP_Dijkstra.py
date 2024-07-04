import heapq

def calculate_conflicts(graph, colors):
    conflicts = 0
    for i in range(len(graph)):
        for j in range(i + 1, len(graph)):
            if graph[i][j] and colors[i] == colors[j]:
                conflicts += 1
    return conflicts

def dijkstra_graph_coloring(graph, num_colors):
    num_nodes = len(graph)
    heap = [(0, [1] * num_nodes)]  # (cost, state)
    visited = set()

    while heap:
        current_cost, current_state = heapq.heappop(heap)

        if tuple(current_state) in visited:
            continue

        visited.add(tuple(current_state))

        if calculate_conflicts(graph, current_state) == 0:
            return current_state

        for color in range(1, num_colors + 1):
            new_state = current_state[:]
            for i in range(num_nodes):
                if new_state[i] != color:
                    new_state[i] = color

                    if tuple(new_state) not in visited:
                        new_cost = current_cost + 1
                        heapq.heappush(heap, (new_cost, new_state))

    return None

# Example usage:
if __name__ == "__main__":
    # Example graph adjacency matrix (undirected):
    graph = [
        [0, 1, 0, 1],
        [1, 0, 1, 0],
        [0, 1, 0, 1],
        [1, 0, 1, 0]
    ]
    num_colors = 3

    best_solution = dijkstra_graph_coloring(graph, num_colors)
    print("Best solution found:", best_solution)
