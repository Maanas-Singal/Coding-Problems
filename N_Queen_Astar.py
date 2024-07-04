import heapq

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

def solve_n_queens_astar(n):
    # Heuristic function (number of conflicts)
    def heuristic(board):
        conflicts = 0
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

    # Priority queue for A* search
    pq = []
    initial_board = [[0] * n for _ in range(n)]
    heapq.heappush(pq, (heuristic(initial_board), initial_board))
    
    while pq:
        _, board = heapq.heappop(pq)
        col = sum(board[i]).index(0) if 1 in board else 0
        
        if col >= n:
            return board
        
        for row in range(n):
            if is_safe(board, row, col):
                new_board = [row[:] for row in board]
                new_board[row][col] = 1
                heapq.heappush(pq, (heuristic(new_board), new_board))
                break

    return None

# Example usage:
n = 8
solution = solve_n_queens_astar(n)
if solution:
    for row in solution:
        print(row)
else:
    print("No solution found.")
