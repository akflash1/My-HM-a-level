class ChessPiece:
    def __init__(self, color, position):
        self.color = color
        self.position = position

    def change_color(self):
        self.color = 'white' if self.color == 'black' else 'black'

    def is_within_board(self, x, y):
        return 0 <= x < 8 and 0 <= y < 8

    def can_move(self, new_position):
        x, y = new_position
        return self.is_within_board(x, y)

class Pawn(ChessPiece):
    def can_move(self, new_position):
        x, y = new_position
        dx = abs(x - self.position[0])
        dy = abs(y - self.position[1])
        if dx == 1 and dy == 0:
            return True
        return False

class Knight(ChessPiece):
    def can_move(self, new_position):
        x, y = new_position
        dx = abs(x - self.position[0])
        dy = abs(y - self.position[1])
        return (dx == 2 and dy == 1) or (dx == 1 and dy == 2)

class Bishop(ChessPiece):
    def can_move(self, new_position):
        x, y = new_position
        dx = abs(x - self.position[0])
        dy = abs(y - self.position[1])
        return dx == dy

class Rook(ChessPiece):
    def can_move(self, new_position):
        x, y = new_position
        return x == self.position[0] or y == self.position[1]

class Queen(ChessPiece):
    def can_move(self, new_position):
        x, y = new_position
        dx = abs(x - self.position[0])
        dy = abs(y - self.position[1])
        return dx == dy or x == self.position[0] or y == self.position[1]

class King(ChessPiece):
    def can_move(self, new_position):
        x, y = new_position
        dx = abs(x - self.position[0])
        dy = abs(y - self.position[1])
        return dx <= 1 and dy <= 1

def get_possible_moves(pieces, new_position):
    valid_pieces = []
    for piece in pieces:
        if piece.can_move(new_position):
            valid_pieces.append(piece)
    return valid_pieces

pawn = Pawn("white", (1, 2))
knight = Knight("black", (3, 2))
bishop = Bishop("white", (2, 3))
rook = Rook("black", (4, 4))
queen = Queen("white", (5, 5))
king = King("black", (6, 6))

chess_pieces = [pawn, knight, bishop, rook, queen, king]

new_position = (3, 3)

possible_moves = get_possible_moves(chess_pieces, new_position)

for piece in possible_moves:
    print(f"{piece.color} {piece.__class__.__name__} can move to {new_position}.")

    