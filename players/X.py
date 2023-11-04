import players.Letter as Letter
import defs.Representation as representation

class X(Letter.Letter):
    def __init__(self, row: int, col: int) -> None:
        super().__init__(row, col)
        self.representation = representation.X
