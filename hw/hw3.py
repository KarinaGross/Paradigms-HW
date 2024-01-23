class TicTacToeGame:
    def __init__(self):
        self.board = ["-" for _ in range(9)]
        self.current_player = "X"

    def print_board(self):
        for row in range(0, 9, 3):
            print(" ".join(self.board[row:row+3]))

    def make_move(self, position):
        if self.board[position] == "-":
            self.board[position] = self.current_player
            return True
        return False

    def check_winner(self):
        lines = [
            (0, 1, 2), (3, 4, 5), (6, 7, 8),  # строки
            (0, 3, 6), (1, 4, 7), (2, 5, 8),  # столбцы
            (0, 4, 8), (2, 4, 6)             # диагонали
        ]
        for a, b, c in lines:
            if self.board[a] == self.board[b] == self.board[c] != "-":
                return True
        return False

    def switch_player(self):
        self.current_player = "O" if self.current_player == "X" else "X"

    def play(self):
        for _ in range(9):
            self.print_board()
            try:
                position = int(input(f"Player {self.current_player}, enter position (from 1 to 9): ")) - 1
                if position in range(9) and self.make_move(position):
                    if self.check_winner():
                        self.print_board()
                        print(f"Игрок {self.current_player} победил!")
                        return
                    self.switch_player()
                else:
                    print("Неверный ход. Попробуйте еще раз.")
            except ValueError:
                print("Неверный ввод. Пожалуйста, введите число.")
                continue
        
        self.print_board()
        print("Ничья!")

game = TicTacToeGame()
game.play()