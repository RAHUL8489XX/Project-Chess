piece_values = {
    "pawn": 1,
    "knight": 3,
    "bishop": 3,
    "rook": 5,
    "queen": 9,
    "king": 1000
}

def evaluate_board(board):
    score = 0
    for row in board:
        for piece in row:
            if piece:
                value = piece_values.get(piece.name, 0)
                score += value if piece.color == "white" else -value
    return score

def get_all_moves(board, color):
    moves = []
    for row in board:
        for piece in row:
            if piece and piece.color == color:
                for move in piece.get_valid_moves(board):
                    moves.append((piece, move))
    return moves

def minimax(board, depth, maximizing_player):
    if depth == 0:
        return evaluate_board(board), None

    color = "white" if maximizing_player else "black"
    best_move = None
    moves = get_all_moves(board, color)

    if maximizing_player:
        max_eval = float('-inf')
        for piece, move in moves:
            original_pos = (piece.row, piece.col)
            captured = board[move[0]][move[1]]
            board[piece.row][piece.col] = None
            piece.move(*move)
            board[move[0]][move[1]] = piece

            eval_score, _ = minimax(board, depth - 1, False)

            board[move[0]][move[1]] = captured
            piece.move(*original_pos)
            board[original_pos[0]][original_pos[1]] = piece

            if eval_score > max_eval:
                max_eval = eval_score
                best_move = (piece, move)
        return max_eval, best_move
    else:
        min_eval = float('inf')
        for piece, move in moves:
            original_pos = (piece.row, piece.col)
            captured = board[move[0]][move[1]]
            board[piece.row][piece.col] = None
            piece.move(*move)
            board[move[0]][move[1]] = piece

            eval_score, _ = minimax(board, depth - 1, True)

            board[move[0]][move[1]] = captured
            piece.move(*original_pos)
            board[original_pos[0]][original_pos[1]] = piece

            if eval_score < min_eval:
                min_eval = eval_score
                best_move = (piece, move)
        return min_eval, best_move
