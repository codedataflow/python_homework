class TictactoeException(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(message)

class Board:
    valid_moves=["upper left",
                 "upper center",
                 "upper right",
                 "middle left",
                 "center",
                 "middle right",
                 "lower left",
                 "lower center",
                 "lower right"]

    def __init__(self):
        self.board_array = [
            [" ", " ", " "],
            [" ", " ", " "],
            [" ", " ", " "],
        ]
        self.turn = "X" # "X" or "O"
        self.turn_count = 0

    def __str__(self):
        return f"Point: x={self.x}, y={self.y}"
    
    def __str__(self):
        lines=[""]
        lines.append(f" {self.board_array[0][0]} | {self.board_array[0][1]} | {self.board_array[0][2]} \n")
        lines.append("-----------\n")
        lines.append(f" {self.board_array[1][0]} | {self.board_array[1][1]} | {self.board_array[1][2]} \n")
        lines.append("-----------\n")
        lines.append(f" {self.board_array[2][0]} | {self.board_array[2][1]} | {self.board_array[2][2]} \n")
        return " ".join(lines)

    # Possible user defined exceptions:
    # - "That's not a valid move." if "move_string" param does not belong to Board.valid_moves
    # - "That spot is taken."
    def move(self, move_string):
        if not move_string in Board.valid_moves:
            raise TictactoeException("That's not a valid move.")
        move_index = Board.valid_moves.index(move_string)
        row = move_index // 3 # row
        column = move_index % 3 #column
        print(f"{move_index} == [{row}, {column}]")
        if self.board_array[row][column] != " ":
            raise TictactoeException("That spot is taken.")
        self.board_array[row][column] = self.turn
        # ternary operator
        self.turn = "O" if self.turn == "X" else "X"
        # self.whats_next()
        self.turn_count += 1
    

    # INCORRECT (original code): if the last possible turn is winning - it will never be resulted to winning game
    # the corrected code is in "whats_next_corrected" function
    def whats_next(self):
        cat = True
        for i in range(3):
            for j in range(3):
                if self.board_array[i][j] == " ":
                    cat = False
                else:
                    continue
                break
            else:
                continue
            break
        if (cat):
            return (True, "Cat's Game.") # INCORRECT: if the last possible turn is winning - it will never be resulted to winning game
        win = False
        for i in range(3): # check rows
            if self.board_array[i][0] != " ":
                if self.board_array[i][0] == self.board_array[i][1] and self.board_array[i][1] == self.board_array[i][2]:
                    win = True
                    break
        if not win:
            for i in range(3): # check columns
                if self.board_array[0][i] != " ":
                    if self.board_array[0][i] == self.board_array[1][i] and self.board_array[1][i] == self.board_array[2][i]:
                        win = True
                        break
        if not win:
            if self.board_array[1][1] != " ": # check diagonals
                if self.board_array[0][0] ==  self.board_array[1][1] and self.board_array[2][2] == self.board_array[1][1]:
                    win = True
                if self.board_array[0][2] ==  self.board_array[1][1] and self.board_array[2][0] == self.board_array[1][1]:
                    win = True
        if not win:
            if self.turn == "X": 
                return (False, "X's turn.")
            else:
                return (False, "O's turn.")
        else:
            if self.turn == "O":
                return (True, "X wins!")
            else:
                return (True, "O wins!")

    # CORRECT (updated code)
    def whats_next_corrected(self):
        win = False
        for i in range(3): # check rows
            if self.board_array[i][0] != " ":
                if self.board_array[i][0] == self.board_array[i][1] and self.board_array[i][1] == self.board_array[i][2]:
                    win = True
                    break
        if not win:
            for i in range(3): # check columns
                if self.board_array[0][i] != " ":
                    if self.board_array[0][i] == self.board_array[1][i] and self.board_array[1][i] == self.board_array[2][i]:
                        win = True
                        break
        if not win:
            if self.board_array[1][1] != " ": # check diagonals
                if self.board_array[0][0] ==  self.board_array[1][1] and self.board_array[2][2] == self.board_array[1][1]:
                    win = True
                if self.board_array[0][2] ==  self.board_array[1][1] and self.board_array[2][0] == self.board_array[1][1]:
                    win = True
        if not win:
            cat = True
            for i in range(3):
                for j in range(3):
                    if self.board_array[i][j] == " ":
                        cat = False
                    else:
                        continue
                    break
                else:
                    continue
                break
            if (cat):
                return (True, "Cat's Game.")
            if self.turn == "X": 
                return (False, "X's turn.")
            else:
                return (False, "O's turn.")
        else:
            if self.turn == "O":
                return (True, "X wins!")
            else:
                return (True, "O wins!")

board = Board()
available_moves = Board.valid_moves.copy()
exit_loop = "exit"

# user input
while True:
    user_move = input(f"[{board.turn}] [Turn: {board.turn_count + 1}/9] Set your move: {available_moves} or type '{exit_loop}': ")
    if user_move == exit_loop:
        break

    board.move(user_move)
    print(board)
    (is_game_over, result) = board.whats_next_corrected() # whats_next()

    if is_game_over:
       print(result)
       break 

    if user_move in available_moves:
        available_moves.remove(user_move)

# using random
"""
import random

while True:
    user_move = random.choice(available_moves) # input(f"[{board.turn}] [Turn: {board.turn_count + 1}/9] Set your move: {available_moves} or type '{exit_loop}': ")
    print(f"[{board.turn}] [Turn: {board.turn_count + 1}/9] Set your move: {available_moves} to {user_move}")
    if user_move == exit_loop:
        break

    board.move(user_move)
    print(board)
    (is_game_over, result) = board.whats_next_corrected() # whats_next()

    if is_game_over:
       print(result)
       break 

    if user_move in available_moves:
        available_moves.remove(user_move)
"""

# Pre-defined sequence of moves: Edge case - Simulate last move wins check in the original code (whats_next()) issue.
"""
moves = [
            'upper left', # X
            'upper right', # O
            'lower right',
            'lower left',
            'upper center',
            'lower center',
            'middle left',
            'middle right',
            'center'
         ]

for user_move in moves:
    print(f"[{board.turn}] [Turn: {board.turn_count + 1}/9] Set your move: {available_moves} to {user_move}")
    if user_move == exit_loop:
        break

    board.move(user_move)
    print(board)
    (is_game_over, result) = board.whats_next()

    if is_game_over:
       print(result)
       break 

    if user_move in available_moves:
        available_moves.remove(user_move)
"""
