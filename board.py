import pygame
from pieces import Pawn, Rook, Knight, Bishop, Piece
from ai import minimax
from pieces import Queen  # Add this to your imports
from pieces import King




class Board:
    def __init__(self, win):
        self.win = win
        self.size = 8
        self.square_size = 80
        self.colors = [(235, 235, 208), (119, 148, 85)]
        self.pieces = []
        self.selected = None
        self.turn = "white"
        self.load_images()
        self.setup_board()
        self.add_piece(Queen("queen", "white", 7, 3, self.images['wq']))
        self.add_piece(Queen("queen", "black", 0, 3, self.images['bq']))
        


    def load_images(self):
        self.images = {name: pygame.image.load(f"assets/{name}.png") for name in [
            'wp','bp','wr','br','wn','bn','wb','bb','wq','bq','wk','bk'
        ]}

    def setup_board(self):
        self.board = [[None for _ in range(8)] for _ in range(8)]
        for col in range(8):
            self.add_piece(Pawn("pawn", "white", 6, col, self.images['wp']))
            self.add_piece(Pawn("pawn", "black", 1, col, self.images['bp']))
        self.add_piece(Rook("rook", "white", 7, 0, self.images['wr']))
        self.add_piece(Rook("rook", "white", 7, 7, self.images['wr']))
        self.add_piece(Rook("rook", "black", 0, 0, self.images['br']))
        self.add_piece(Rook("rook", "black", 0, 7, self.images['br']))
        self.add_piece(Knight("knight", "white", 7, 1, self.images['wn']))
        self.add_piece(Knight("knight", "white", 7, 6, self.images['wn']))
        self.add_piece(Knight("knight", "black", 0, 1, self.images['bn']))
        self.add_piece(Knight("knight", "black", 0, 6, self.images['bn']))
        self.add_piece(Bishop("bishop", "white", 7, 2, self.images['wb']))
        self.add_piece(Bishop("bishop", "white", 7, 5, self.images['wb']))
        self.add_piece(Bishop("bishop", "black", 0, 2, self.images['bb']))
        self.add_piece(Bishop("bishop", "black", 0, 5, self.images['bb']))
        self.add_piece(Piece("queen", "white", 7, 3, self.images['wq']))
        self.add_piece(Piece("queen", "black", 0, 3, self.images['bq']))
        self.add_piece(Piece("king", "white", 7, 4, self.images['wk']))
        self.add_piece(Piece("king", "black", 0, 4, self.images['bk']))

    def add_piece(self, piece):
        self.pieces.append(piece)
        self.board[piece.row][piece.col] = piece

    def draw(self):
        for row in range(self.size):
            for col in range(self.size):
                color = self.colors[(row + col) % 2]
                pygame.draw.rect(self.win, color,
                                 (col * self.square_size, row * self.square_size,
                                  self.square_size, self.square_size))
        for piece in self.pieces:
            piece.draw(self.win, self.square_size)
        if self.selected:
            for r, c in self.selected.get_valid_moves(self.board):
                pygame.draw.rect(self.win, (0, 255, 0),
                                 (c * self.square_size, r * self.square_size,
                                  self.square_size, self.square_size), 3)
        pygame.display.update()
    
    def make_ai_move(self):
        _, best_move = minimax(self.board, depth=2, maximizing_player=False)
        if best_move:
            piece, move = best_move
            captured = self.board[move[0]][move[1]]
            self.board[piece.row][piece.col] = None
            piece.move(*move)
            self.board[move[0]][move[1]] = piece
            if captured:
                self.pieces.remove(captured)
            self.turn = "white"

    def handle_click(self, pos):
        col = pos[0] // self.square_size
        row = pos[1] // self.square_size
        clicked_piece = self.board[row][col]

        if self.selected:
            if (row, col) in self.selected.get_valid_moves(self.board):
                if self.selected.color == self.turn:
                    captured = self.board[row][col]
                        # 👇 This block handles movement and captures
                    self.board[self.selected.row][self.selected.col] = None
                    self.selected.move(row, col)
                    self.board[row][col] = self.selected

                    if captured:
                        self.pieces.remove(captured)
                    self.turn = 'black'
                    self.make_ai_move()
            self.selected = None

        elif clicked_piece and clicked_piece.color == self.turn:
            self.selected = clicked_piece

    

def is_in_check(board, color):
    # Find king position
    for row in board:
        for piece in row:
            if piece and piece.name == "king" and piece.color == color:
                king_pos = (piece.row, piece.col)

    # Check if any opponent piece can move to king's position
    for row in board:
        for piece in row:
            if piece and piece.color != color:
                if king_pos in piece.get_valid_moves(board):
                    return True
    return False
