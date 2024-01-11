from copy import deepcopy
import pygame

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)


def minMax(position, depth, max_player, game):
    if depth == 0 or position.winner() != None:
        return position.evaluate(), position

    if max_player:
        maxEval = float('-inf')
        best_move = None
        for move in successors(position, WHITE, game):
            evaluation = minMax(move, depth - 1, False, game)[0]
            maxEval = max(maxEval, evaluation)
            if maxEval == evaluation:
                best_move = move

        return maxEval, best_move
    else:
        minEval = float('inf')
        best_move = None
        for move in successors(position, BLACK, game):
            evaluation = minMax(move, depth - 1, True, game)[0]
            minEval = min(minEval, evaluation)
            if minEval == evaluation:
                best_move = move

        return minEval, best_move


def minMaxWithAB(position, depth, alpha, beta, max_player, game):
    if depth == 0 or position.winner() is not None:
        return position.evaluate(), position

    if max_player:
        maxEval = float('-inf')
        best_move = None
        for move in successors(position, WHITE, game):
            evaluation = minMaxWithAB(move, depth - 1, alpha, beta, False, game)[0]
            maxEval = max(maxEval, evaluation)
            if beta <= alpha:
                break
            if maxEval > alpha:
                alpha = maxEval
                best_move = move

        return maxEval, best_move
    else:
        minEval = float('inf')
        best_move = None
        for move in successors(position, BLACK, game):
            evaluation = minMaxWithAB(move, depth - 1, alpha, beta, True, game)[0]
            minEval = min(minEval, evaluation)
            if beta <= alpha:
                break
            if minEval < beta:
                beta = minEval
                best_move = move

        return minEval, best_move


def simulate_move(piece, move, board, game, skip):
    board.move(piece, move[0], move[1])
    if skip:
        board.remove(skip)

    return board


def draw_moves(game, board, piece):
    valid_moves = board.get_successors(piece)
    board.draw(game.win)
    pygame.draw.circle(game.win, (0,255,0), (piece.x, piece.y), 50, 5)
    game.draw_valid_moves(valid_moves.keys())
    #pygame.display.update()
    #pygame.time.delay(100)


def successors(board, color, game):
    moves = []

    for piece in board.get_all_pieces(color):
        valid_moves = board.get_successors(piece)
        for move, skip in valid_moves.items():
            draw_moves(game, board, piece)
            temp_board = deepcopy(board)
            temp_piece = temp_board.get_piece(piece.row, piece.col)
            new_board = simulate_move(temp_piece, move, temp_board, game, skip)
            moves.append(new_board)
    
    return moves