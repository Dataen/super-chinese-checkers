from .piece import Piece
from .helper import *


class Hex():

    _id = 0
    _piece = 0
    _owner = 0
    _neighbours = []

    def __init__(self, id):
        self._id = id
        self._neighbours = [-1] * 6

    def __str__(self):
        return str(self._id)

    def set_piece(self, id):
        self._piece = id

    def get_piece(self):
        return self._piece

    def has_piece(self):
        return self._piece > 0

    def get_id(self):
        return self._id

    def set_neighbour(self, dir, other_hex):
        self._neighbours[dir.value] = other_hex.get_id()

    def get_neighbour(self, dir):
        return self._neighbours[dir.value]

    def has_neighbour(self, dir):
        return self._neighbours[dir.value] >= 0

    def get_neighbours(self):
        return self._neighbours

    def set_owner(self, owner):
        self._owner = owner

    def has_owner(self):
        return self._owner > 0

    def get_owner(self):
        return self._owner
