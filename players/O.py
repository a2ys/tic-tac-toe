import Letter
import defs.Representation as representation

class O(Letter.Letter):
    def __init__(self, row: int, col: int) -> None:
        super().__init__(row, col)
        self.representation = representation.O
