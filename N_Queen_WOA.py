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

def initialize_whales(num_whales, n):
    whales = []
    for _ in range(num_whales):
        positions = [random.randint(0, n-1) for _ in range(n)]
        whales.append((positions, count_conflicts(create_board(positions, n))))
    return whales

def update_search_agent_position(agent, global_best_positions, a, n):
    positions, conflicts = agent
    rand_leader = random.randint(0, len(global_best_positions) - 1)
    r1 = random.random()
    r2 = random.random()
    A = 2 * a * r1 - a
    C = 2 * r2
    l = random.uniform(-1, 1)
    
    p = random.random()
    if p < 0.5:
        if abs(A) < 1:
            for i, pos in enumerate(positions):
                d = abs(global_best_positions[rand_leader][i] - pos)
                positions[i] = global_best_positions[rand_leader][i] - A * d
        else:
            for i, pos in enumerate(positions):
                d = abs(global_best_positions[rand_leader][i] - pos)
                positions[i] = global_best_positions[rand_leader][i] + A * d
    else:
        for i, pos in enumerate(positions):
            d1 = abs(global_best_positions[rand_leader][i] - pos)
            positions[i] = d1 * np.exp(b * l) * np.cos(2 * np.pi * l) + global_best_positions[rand_leader][i]

    # Ensure positions are within bounds
    for i in range(len(positions)):
        if positions[i] < 0:
            positions[i] = 0
        elif positions[i] >= n:
            positions[i] = n - 1
    
    new_conflicts = count_conflicts(create_board(positions, n))
    return positions, new_conflicts

def woa_n_queens(num_whales, n, max_iterations):
    a = 0.5  # constant
    whales = initialize_whales(num_whales, n)
    global_best_positions = None
    global_best = float('inf')
    
    for _ in range(max_iterations):
        for i, whale in enumerate(whales):
            positions, conflicts = whale
            if conflicts == 0:
                return create_board(positions, n)
            if conflicts < global_best:
                global_best = conflicts
                global_best_positions = positions
            
            new_positions, new_conflicts = update_search_agent_position(whale, global_best_positions, a, n)
            whales[i] = (new_positions, new_conflicts)
    
    return None

# Example usage:
num_whales = 10
n = 8
max_iterations = 100
solution = woa_n_queens(num_whales, n, max_iterations)
if solution:
    for row in solution:
        print(row)
else:
    print("No solution found.")
