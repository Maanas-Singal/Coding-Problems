import random
import numpy as np

def is_safe(board, row, col):
    """ Check if it's safe to place a queen at board[row][col] """
    # Check this row on left side
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper diagonal on left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check lower diagonal on left side
    for i, j in zip(range(row, len(board), 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True

def count_conflicts(board):
    conflicts = 0
    n = len(board)
    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:
                for k in range(j + 1, n):
                    if board[i][k] == 1:
                        conflicts += 1
                for k in range(1, n - i):
                    if i + k < n and j + k < n and board[i + k][j + k] == 1:
                        conflicts += 1
                for k in range(1, i + 1):
                    if i - k >= 0 and j + k < n and board[i - k][j + k] == 1:
                        conflicts += 1
    return conflicts

def create_board(positions, n):
    board = [[0] * n for _ in range(n)]
    for col, row in enumerate(positions):
        board[row][col] = 1
    return board

def initialize_particles(num_particles, n):
    particles = []
    for _ in range(num_particles):
        positions = [random.randint(0, n-1) for _ in range(n)]
        particles.append((positions, count_conflicts(create_board(positions, n))))
    return particles

def update_velocity(particle, global_best, w, c1, c2):
    positions, conflicts = particle
    velocities = []
    for pos in positions:
        r1, r2 = random.random(), random.random()
        velocity = w * pos + c1 * r1 * (global_best - pos) + c2 * r2 * (global_best - pos)
        velocities.append(velocity)
    return velocities

def update_position(positions, velocities, n):
    new_positions = []
    for i, pos in enumerate(positions):
        new_pos = int(round(pos + velocities[i]))
        if new_pos < 0:
            new_pos = 0
        elif new_pos >= n:
            new_pos = n - 1
        new_positions.append(new_pos)
    return new_positions

def pso_n_queens(num_particles, n, max_iterations):
    w = 0.5  # inertia weight
    c1 = 1.5  # cognitive weight
    c2 = 1.5  # social weight
    global_best = float('inf')
    global_best_positions = None
    particles = initialize_particles(num_particles, n)
    
    for _ in range(max_iterations):
        for i, particle in enumerate(particles):
            positions, conflicts = particle
            if conflicts == 0:
                return create_board(positions, n)
            if conflicts < global_best:
                global_best = conflicts
                global_best_positions = positions
            
            velocities = update_velocity(particle, global_best_positions, w, c1, c2)
            new_positions = update_position(positions, velocities, n)
            new_conflicts = count_conflicts(create_board(new_positions, n))
            particles[i] = (new_positions, new_conflicts)
            
    return None

# Example usage:
num_particles = 20
n = 8
max_iterations = 100
solution = pso_n_queens(num_particles, n, max_iterations)
if solution:
    for row in solution:
        print(row)
else:
    print("No solution found.")
