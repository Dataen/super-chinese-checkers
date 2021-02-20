from SCC.board import Board
from SCC.helper import Direction
import sys

import os
from flask import Flask, send_from_directory, make_response

app = Flask(__name__, static_folder='react_app/build')

# Serve React App


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def serve(path):
    if path != "" and os.path.exists(app.static_folder + '/' + path):
        return send_from_directory(app.static_folder, path)
    else:
        return send_from_directory(app.static_folder, 'index.html')

@app.route('/getnewboard')
def getnewboard():
    board = Board()
    hexes = board.get_hexes()
    obj = []
    for h in hexes:
        id = h.get_id()
        piece = h.get_piece()
        obj.append({'id': id, 'piece': piece})
    resp = make_response({'board': obj}, 200)
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp


if __name__ == '__main__':
    app.run(use_reloader=True, port=5000, threaded=True)


# @app.route('/')
# def hello_world():
#     board = Board()
#     all_moves = board.get_all_moves()

#     string = ""

#     for i in range(121):
#         hex_moves = all_moves[i]
#         string = string + str(i) + ": "
#         for move in hex_moves:
#             string = string + str(move) + ", "
#         string = string + "\n"

#     return string
