import pygame
from .constants import WHITE, BLACK, GREEN, SQUARE_SIZE
from checkers.board import Board


class Game:
    def __init__(self, win):
        self._init()
        self.win = win

    def update(self):
        self.board.draw(self.win)
        self.draw_valid_moves(self.valid_moves)
        pygame.display.update()
    
    def _init(self):
        self.selected = None
        self.board = Board()
        self.turn = WHITE
        self.valid_moves = {}

    def reset(self):
        _init()

    def select(self, row, col):
        if self.selected:
            result = self._move(row, col)
            if not result:
               self.selected = None
               self.select(row, col)
        else:
            piece = self.board.get_piece(row, col)
            if piece != 0 and piece.colour == self.turn:
                self.selected = piece
                self.valid_moves = self.board.get_valid_moves(piece)
                return True
        return False
         
    def _move(self, row, col):
        piece = self.board.get_piece(row, col)
        if self.select and piece == 0 and (row, col) in self.valid_moves:
            self.board.move(self.selected, row, col)
        else:
             return False
        return True
    
    def change_turn(self):
        if self.turn == WHITE:
            self.turn = BLACK
        else:
            self.turn = WHITE
    
    def draw_valid_moves(self, moves):
        for move in moves:
            row, col = move
            pygame.draw.circle(self.win, GREEN, (col * SQUARE_SIZE + SQUARE_SIZE//2, row * SQUARE_SIZE + SQUARE_SIZE//2), 15)