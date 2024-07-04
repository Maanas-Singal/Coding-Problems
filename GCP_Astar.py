import heapq

class Node:
    def __init__(self, state, parent=None, cost=0, heuristic=0):
        self.state = state
        self.parent = parent
        self.cost = cost
        self.heuristic = heuristic
        self.total_cost = cost + heuristic

def calculate_conflicts(graph, colors):
    conflicts = 0
    for i in range(len(graph)):
        for j in range(i + 1, len(graph)):
            if graph[i][j] and colors[i] == colors[j]:
                conflicts += 1
    return conflicts

def graph_coloring_astar(graph, num_colors):
    initial_state = [1] * len(graph)  # Start with all nodes colored with the first color
    open_list = [Node(initial_state, None, 0, calculate_conflicts(graph, initial_state))]
    closed_list = set()

    while open_list:
        current_node = heapq.heappop(open_list)

        if current_node.heuristic == 0:
            solution = current_node.state
            return solution

        closed_list.add(tuple(current_node.state))

        for color in range(1, num_colors + 1):
            new_state = current_node.state[:]
            for i in range(len(new_state)):
                if new_state[i] != color:
                    new_state[i] = color

                    if tuple(new_state) not in closed_list:
                        new_cost = current_node.cost + 1
                        new_heuristic = calculate_conflicts(graph, new_state)
                        new_node = Node(new_state, current_node, new_cost, new_heuristic)
                        heapq.heappush(open_list, new_node)

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

    best_solution = graph_coloring_astar(graph, num_colors)
    print("Best solution found:", best_solution)
