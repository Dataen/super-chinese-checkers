from SCC.board import Board
from SCC.helper import Direction
import sys

from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello_world():
    board = Board()
    all_moves = board.get_all_moves()

    string = ""

    for i in range(121):
        hex_moves = all_moves[i]
        string = string + str(i) + ": "
        for move in hex_moves:
            string = string + str(move) + ", "
        string = string + "\n"

    return string
