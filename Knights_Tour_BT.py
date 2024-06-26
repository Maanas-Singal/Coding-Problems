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
    """
    # Initialize the board with -1 (unvisited)
    board = [[-1 for _ in range(m)] for _ in range(n)]

    # Possible moves for a knight
    move_x = [2, 1, -1, -2, -2, -1, 1, 2]
    move_y = [1, 2, 2, 1, -1, -2, -2, -1]

    # Starting position (0, 0)
    board[0][0] = 0

    # Counter for number of moves
    move_count = 1

    # Recursive function to find the Knight's Tour using backtracking
    def solve_knights_tour(x, y, move_count):
        # Base case: if all squares are visited
        if move_count == n * m:
            return True

        # Try all next moves from the current coordinate
        for i in range(8):
            next_x = x + move_x[i]
            next_y = y + move_y[i]
            if is_valid_move(board, n, m, next_x, next_y):
                board[next_x][next_y] = move_count
                # Print the board after each move attempt
                print_board(board)
                if solve_knights_tour(next_x, next_y, move_count + 1):
                    return True
                # Backtrack
                board[next_x][next_y] = -1

        return False

    def print_board(board):
        """
        Function to print the board in a readable format
        """
        for row in board:
            print(row)
        print("\n")

    # Start the recursion from the top-left corner (0, 0)
    if not solve_knights_tour(0, 0, move_count):
        print("Solution does not exist")

# Example usage:
knights_tour(8, 8)  # Change dimensions as per your requirement (n, m)
