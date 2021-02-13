from .hex import Hex
from .helper import *


class Board():

    _hexes = []

    def __init__(self):
        self.new()

    def new(self):
        self._hexes = get_new_board()

    def get_hexes(self):
        return self._hexes

    def get_all_moves(self):
        tuples = get_possible_moves(self._hexes)
        return tuples

    def get_moves(self, hex_id):
        tuples = get_moves_hex(self._hexes[hex_id], self._hexes)
        return tuples

    def make_move(self, id_from, id_to):
        h_from = self._hexes[id_from]

        if not h_from.has_piece():
            print("No piece")

        moves = self.get_moves(id_from)
        if id_to in moves:
            h_to = self._hexes[id_to]
            piece = h_from.get_piece()
            h_to.set_piece(piece)
            h_from.set_piece(0)
        else:
            print("Invalid move")
