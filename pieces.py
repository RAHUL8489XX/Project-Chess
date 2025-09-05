class Piece:
    def __init__(self, name, color, row, col, image):
        self.name = name
        self.color = color
        self.row = row
        self.col = col
        self.image = image

    def draw(self, win, square_size):
        x = self.col * square_size
        y = self.row * square_size
        win.blit(self.image, (x, y))

    def move(self, row, col):
        self.row = row
        self.col = col

    def get_valid_moves(self, board):
        return []

class Pawn(Piece):
    def get_valid_moves(self, board):
        direction = -1 if self.color == "white" else 1
        moves = []
        r = self.row + direction
        if 0 <= r < 8 and board[r][self.col] is None:
            moves.append((r, self.col))
        return moves

class Rook(Piece):
    def get_valid_moves(self, board):
        moves = []
        for dr, dc in [(1,0), (-1,0), (0,1), (0,-1)]:
            r, c = self.row + dr, self.col + dc
            while 0 <= r < 8 and 0 <= c < 8:
                if board[r][c] is None:
                    moves.append((r, c))
                elif board[r][c].color != self.color:
                    moves.append((r, c))
                    break
                else:
                    break
                r += dr
                c += dc
        return moves

class Bishop(Piece):
    def get_valid_moves(self, board):
        moves = []
        for dr, dc in [(1,1), (1,-1), (-1,1), (-1,-1)]:
            r, c = self.row + dr, self.col + dc
            while 0 <= r < 8 and 0 <= c < 8:
                if board[r][c] is None:
                    moves.append((r, c))
                elif board[r][c].color != self.color:
                    moves.append((r, c))
                    break
                else:
                    break
                r += dr
                c += dc
        return moves

class Knight(Piece):
    def get_valid_moves(self, board):
        moves = []
        for dr, dc in [(2,1), (1,2), (-1,2), (-2,1), (-2,-1), (-1,-2), (1,-2), (2,-1)]:
            r, c = self.row + dr, self.col + dc
            if 0 <= r < 8 and 0 <= c < 8:
                if board[r][c] is None or board[r][c].color != self.color:
                    moves.append((r, c))
        return moves

class Queen(Piece):
    def get_valid_moves(self, board):
        moves = []
        directions = [
            (1, 0), (-1, 0), (0, 1), (0, -1),  # Rook-like
            (1, 1), (1, -1), (-1, 1), (-1, -1) # Bishop-like
        ]
        for dr, dc in directions:
            r, c = self.row + dr, self.col + dc
            while 0 <= r < 8 and 0 <= c < 8:
                if board[r][c] is None:
                    moves.append((r, c))
                elif board[r][c].color != self.color:
                    moves.append((r, c))  # Capture
                    break
                else:
                    break
                r += dr
                c += dc
        return moves

class King(Piece):
    def get_valid_moves(self, board):
        moves = []
        directions = [
            (1, 0), (-1, 0), (0, 1), (0, -1),
            (1, 1), (1, -1), (-1, 1), (-1, -1)
        ]
        for dr, dc in directions:
            r, c = self.row + dr, self.col + dc
            if 0 <= r < 8 and 0 <= c < 8:
                if board[r][c] is None or board[r][c].color != self.color:
                    moves.append((r, c))
        return moves
