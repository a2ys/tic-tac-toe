import players.Empty


class Board:
    def __init__(self) -> None:
        self.board = [[players.Empty.Empty(row, col) for col in range(3)] for row in range(3)]

    def display_board(self) -> None:
        for row in self.board:
            for player in row:
                print(player.get_representation(), end=" | ")
            print()
