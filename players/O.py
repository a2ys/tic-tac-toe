import players.Letter as Letter
import defs.Representation as Representation

class O(Letter.Letter):
    def __init__(self, row: int, col: int) -> None:
        super().__init__(row, col)
        self.representation = Representation.O
