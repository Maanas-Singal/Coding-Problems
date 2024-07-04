import random

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

def initialize_harmonies(num_harmonies, n):
    harmonies = []
    for _ in range(num_harmonies):
        positions = [random.randint(0, n-1) for _ in range(n)]
        harmonies.append((positions, count_conflicts(create_board(positions, n))))
    return harmonies

def update_harmony(new_harmony, n, hmcr, par):
    positions, _ = new_harmony
    new_positions = positions[:]
    r = random.random()
    if r < hmcr:
        rand_index = random.randint(0, len(positions) - 1)
        new_positions[rand_index] = par[rand_index]
    else:
        rand_indexes = random.sample(range(len(positions)), 2)
        new_positions[rand_indexes[0]] = random.randint(0, n - 1)
        new_positions[rand_indexes[1]] = random.randint(0, n - 1)
    
    new_conflicts = count_conflicts(create_board(new_positions, n))
    return new_positions, new_conflicts

def hbo_n_queens(num_harmonies, n, max_iterations, hmcr=0.85, par=None):
    if par is None:
        par = [random.randint(0, n-1) for _ in range(n)]
    
    harmonies = initialize_harmonies(num_harmonies, n)
    global_best_positions = None
    global_best = float('inf')
    
    for _ in range(max_iterations):
        for i, harmony in enumerate(harmonies):
            positions, conflicts = harmony
            if conflicts == 0:
                return create_board(positions, n)
            if conflicts < global_best:
                global_best = conflicts
                global_best_positions = positions
            
            new_positions, new_conflicts = update_harmony(harmony, n, hmcr, par)
            harmonies[i] = (new_positions, new_conflicts)
    
    return None

# Example usage:
num_harmonies = 20
n = 8
max_iterations = 100
solution = hbo_n_queens(num_harmonies, n, max_iterations)
if solution:
    for row in solution:
        print(row)
else:
    print("No solution found.")
