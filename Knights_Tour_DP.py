import heapq

def is_valid_move(board, n, m, x, y):
    """
    Check if the move (x, y) is valid on the board of size n x m
    """
    if 0 <= x < n and 0 <= y < m and board[x][y] == -1:
        return True
    return False

def knights_tour(n, m):
    """
    Function to solve the Knight's Tour problem on an n x m chessboard
    with visual representation using A* algorithm
    """
    # Initialize the board with -1 (unvisited)
    board = [[-1 for _ in range(m)] for _ in range(n)]

    # Possible moves for a knight
    move_x = [2, 1, -1, -2, -2, -1, 1, 2]
    move_y = [1, 2, 2, 1, -1, -2, -2, -1]

    # Starting position (0, 0)
    board[0][0] = 0

    # Priority queue for A* algorithm (stores tuples of (cost, x, y))
    pq = []
    heapq.heappush(pq, (0, 0, 0, 0))  # (cost, move_count, x, y)

    # Counter for number of moves
    move_count = 1

    def heuristic(x, y, n, m):
        """
        Heuristic function to estimate the remaining moves to complete the tour
        """
        # Minimum remaining moves to complete the tour
        return (n * m - move_count)

    while pq:
        _, current_cost, x, y = heapq.heappop(pq)

        # Try all next moves from the current coordinate
        for i in range(8):
            next_x = x + move_x[i]
            next_y = y + move_y[i]
            if is_valid_move(board, n, m, next_x, next_y):
                board[next_x][next_y] = move_count
                # Print the board after each move attempt
                print_board(board)
                if move_count == n * m - 1:
                    print("Solution found!")
                    return
                next_cost = current_cost + 1 + heuristic(next_x, next_y, n, m)
                heapq.heappush(pq, (next_cost, current_cost + 1, next_x, next_y))
                move_count += 1

    print("Solution does not exist")

def print_board(board):
    """
    Function to print the board in a readable format
    """
    for row in board:
        print(row)
    print("\n")

# Example usage:
knights_tour(8, 8)  # Change dimensions as per your requirement (n, m)
