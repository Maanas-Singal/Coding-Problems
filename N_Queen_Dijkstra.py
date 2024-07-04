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

def solve_n_queens_dijkstra(n):
    # Dijkstra's algorithm for N-Queens problem
    # Priority queue to store (cost, board)
    pq = []
    heapq.heappush(pq, (0, [[0] * n for _ in range(n)]))  # Initial cost and board
    
    while pq:
        cost, board = heapq.heappop(pq)
        col = sum(board[i]).index(0) if 1 in board else 0
        
        if col >= n:
            return board
        
        for row in range(n):
            if is_safe(board, row, col):
                new_board = [row[:] for row in board]
                new_board[row][col] = 1
                new_cost = cost + 1  # Assuming uniform cost for transitions
                heapq.heappush(pq, (new_cost, new_board))
                break

    return None

# Example usage:
n = 8
solution = solve_n_queens_dijkstra(n)
if solution:
    for row in solution:
        print(row)
else:
    print("No solution found.")
