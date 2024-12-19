"""
The Mini Game problem from Karat involves simulating a simple game where players take turns to make moves on a game board. The objective is to determine the winner based on the game's rules.

Problem Statement:

You are tasked with simulating a simple game played on a 3x3 board. The game is played by two players who take turns to place their marks ('X' and 'O') on the board. The first player to align three of their marks horizontally, vertically, or diagonally wins the game.

Input:

A list of moves, where each move is represented as a tuple (row, col) indicating the position on the board where the player places their mark.
Output:

Return the winner of the game ('X' or 'O') if there is one.
If the game ends in a draw (i.e., all positions are filled without a winner), return 'Draw'.
If the game is still ongoing (i.e., there are empty positions and no winner yet), return 'Ongoing'.
Example:

moves = [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]
result = mini_game(moves)
print(result)  # Output: 'Draw'
Constraints:

The list of moves will contain between 1 and 9 tuples.
Each tuple (row, col) represents a valid position on the 3x3 board.
The moves are provided in the order they are made, starting with player 'X'.
Note:

The game board is indexed from 0 to 2 for both rows and columns.
The game ends immediately when a player wins, and no further moves are made.


"""

def mini_game(moves):
    # Initialize a 3x3 board
    board = [['' for _ in range(3)] for _ in range(3)]
    
    # Function to check if a player has won
    def check_winner(player):
        # Check rows, columns, and diagonals
        for i in range(3):
            if all(board[i][j] == player for j in range(3)):  # Check row
                return True
            if all(board[j][i] == player for j in range(3)):  # Check column
                return True
        if all(board[i][i] == player for i in range(3)):  # Check diagonal (top-left to bottom-right)
            return True
        if all(board[i][2-i] == player for i in range(3)):  # Check diagonal (top-right to bottom-left)
            return True
        return False
    
    # Iterate through the moves
    for idx, (row, col) in enumerate(moves):
        player = 'X' if idx % 2 == 0 else 'O'  # 'X' plays at even indices, 'O' at odd indices
        board[row][col] = player
        
        # Check if the current player has won
        if check_winner(player):
            return player
    
    # If the board is full and no one won, it's a draw
    if len(moves) == 9:
        return 'Draw'
    
    # If there are still empty spaces and no winner, the game is ongoing
    return 'Ongoing'

# Example usage:
moves = [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]
result = mini_game(moves)
print(result)  # Output: 'Draw'


""""Time Complexity:
Check Winner: Each winner check involves checking 3 rows, 3 columns, and 2 diagonals, which is O(1).
Overall: The game processes up to 9 moves, so the time complexity is O(9) = O(1), since the board is fixed at 3x3.
Space Complexity:
The space complexity is O(1) as the board is always a fixed 3x3 matrix."""