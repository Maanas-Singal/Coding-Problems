import random
import numpy as np

def is_valid_move(board, n, m, x, y):
    """
    Check if the move (x, y) is valid on the board of size n x m
    """
    if 0 <= x < n and 0 <= y < m and board[x][y] == -1:
        return True
    return False

def knights_tour_pso(n, m, num_particles=10, num_iterations=100):
    """
    Function to solve the Knight's Tour problem on an n x m chessboard
    with visual representation using Particle Swarm Optimization (PSO)
    """
    # Initialize the board with -1 (unvisited)
    board = [[-1 for _ in range(m)] for _ in range(n)]

    # Possible moves for a knight
    move_x = [2, 1, -1, -2, -2, -1, 1, 2]
    move_y = [1, 2, 2, 1, -1, -2, -2, -1]

    # Initialize particles with random starting positions
    particles = []
    for _ in range(num_particles):
        start_x, start_y = random.randint(0, n-1), random.randint(0, m-1)
        particles.append((start_x, start_y))

    global_best_position = None
    global_best_cost = float('inf')

    for _ in range(num_iterations):
        for i, (current_x, current_y) in enumerate(particles):
            # Initialize board and move count for this particle
            board[current_x][current_y] = 0
            move_count = 1

            # Perform Knight's Tour from current position
            while move_count < n * m:
                possible_moves = []
                for j in range(8):
                    next_x = current_x + move_x[j]
                    next_y = current_y + move_y[j]
                    if is_valid_move(board, n, m, next_x, next_y):
                        possible_moves.append((next_x, next_y))

                if not possible_moves:
                    break

                # Choose next move randomly for PSO simplicity
                next_x, next_y = random.choice(possible_moves)
                board[next_x][next_y] = move_count
                current_x, current_y = next_x, next_y
                move_count += 1

            # Evaluate cost (number of moves) for this particle's tour
            cost = np.sum(board)  # Sum of all elements in board is the cost

            # Update global best if this particle found a better solution
            if cost < global_best_cost:
                global_best_cost = cost
                global_best_position = particles[i]

            # Clear the board for the next iteration
            board = [[-1 for _ in range(m)] for _ in range(n)]

        # Update particles positions (randomly)
        for i in range(num_particles):
            particles[i] = (random.randint(0, n-1), random.randint(0, m-1))

        # Print the board with global best position after each iteration
        print("Iteration:", _+1)
        print_board_with_best(board, global_best_position, n, m)
        print("Global Best Cost:", global_best_cost)
        print()

    # Final board with the global best position
    print("Final Solution:")
    print_board_with_best(board, global_best_position, n, m)
    print("Global Best Cost:", global_best_cost)

def print_board_with_best(board, best_position, n, m):
    """
    Function to print the board with current best position in a readable format
    """
    for i in range(n):
        for j in range(m):
            if (i, j) == best_position:
                print("X", end=' ')
            else:
                print(board[i][j], end=' ')
        print()

    print()

# Example usage:
knights_tour_pso(8, 8, num_particles=10, num_iterations=20)
