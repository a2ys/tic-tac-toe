import defs.Representation as Representation


class Letter:
    def __init__(self, row: int, col: int) -> None:
        self.row = row
        self.col = col
        self.pos = (self.row, self.col)
        self.representation = Representation.EMPTY
    
    def get_pos(self) -> tuple[int, int]:
        return self.pos

    def set_pos(self, pos: tuple[int, int]) -> None:
        self.pos = pos
    
    def get_representation(self) -> str:
        return self.representation
    
    def set_representation(self, repr: Representation) -> None:
        self.representation = repr
