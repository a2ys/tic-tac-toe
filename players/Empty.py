import players.Letter as Letter

class Empty(Letter.Letter):
    def __init__(self, row: int, col: int) -> None:
        super().__init__(row, col)
