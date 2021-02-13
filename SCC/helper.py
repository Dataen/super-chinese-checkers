import SCC

try:
    import importlib.resources as pkg_resources
except ImportError:
    # Try backported to PY<37 `importlib_resources`.
    import importlib_resources as pkg_resources

from . import boards

from enum import Enum


class Direction(Enum):
    LEFT = 0
    RIGHT = 1
    TOP_LEFT = 2
    TOP_RIGHT = 3
    BOTTOM_LEFT = 4
    BOTTOM_RIGHT = 5


def read_default_board_lines():
    return pkg_resources.open_text(boards, "default.txt").readlines()


def get_new_board():
    hexes = []
    lines = read_default_board_lines()

    hex_id = 0

    last_line_ids = [-1]*17
    last_hex_id = 0

    for line in lines:
        chars = list(line)
        x = 0
        current_line = []
        for char in chars:
            if char.isnumeric():
                h = SCC.hex.Hex(hex_id)
                h.set_piece(int(char))
                h.set_owner(int(char))

                # Setup neighbours
                if last_hex_id >= 0:  # LEFT
                    h.set_neighbour(Direction.LEFT, hexes[last_hex_id])
                    hexes[last_hex_id].set_neighbour(Direction.RIGHT, h)

                if last_line_ids[x] >= 0:  # TOP_RIGHT
                    h.set_neighbour(Direction.TOP_RIGHT, hexes[last_line_ids[x]])
                    hexes[last_line_ids[x]].set_neighbour(Direction.BOTTOM_LEFT, h)

                if x-1 >= 0 and last_line_ids[x-1] >= 0:  # TOP_LEFT
                    h.set_neighbour(Direction.TOP_LEFT, hexes[last_line_ids[x-1]])
                    hexes[last_line_ids[x-1]].set_neighbour(Direction.BOTTOM_RIGHT, h)

                current_line.append(hex_id)
                last_hex_id = hex_id
                hexes.append(h)
                hex_id += 1
            else:
                current_line.append(-1)
                last_hex_id = -1

            x += 1

        last_line_ids = current_line

    return hexes


def get_opponent(player):
    opps = [2, 1, 4, 3, 6, 5]
    return opps[player - 1]


def get_hexes_in_line(h, dir, hexes):
    line = [h]
    while True:
        next_hex = line[len(line) - 1]
        if next_hex.has_neighbour(dir):
            line.append(hexes[next_hex.get_neighbour(dir)])
        else:
            return line


def line_segment_has_symmetry(line, end):
    to_middle = int((end - 1) / 2)
    for i in range(1, to_middle + 1):
        if not line[i].has_piece() == line[end - i].has_piece():
            return False
    return True


def has_visited(h, visited):
    return h.get_id() in visited


def get_available_hexes_in_line_from(h, dir, hexes, visited):
    line = get_hexes_in_line(h, dir, hexes)
    possible = []
    has_jumped_over_piece = False

    check_to_dynamic = int((len(line) + 1) / 2)

    for i in range(1, check_to_dynamic):
        end_hex = line[i]
        if has_jumped_over_piece:
            if not end_hex.has_piece() and not has_visited(end_hex, visited):
                if line_segment_has_symmetry(line, i):
                    possible.append(end_hex.get_id())
                    i += i - 1  # Skipping impossible iterations
        elif end_hex.has_piece():
            check_to_dynamic = len(line)
            i += i - 1
            has_jumped_over_piece = True

    return possible


def get_available_hexes_in_all_directions_from(h, hexes, visited):
    all_dirs = []
    all_dirs += get_available_hexes_in_line_from(h, Direction.TOP_LEFT, hexes, visited)
    all_dirs += get_available_hexes_in_line_from(h, Direction.TOP_RIGHT, hexes, visited)
    all_dirs += get_available_hexes_in_line_from(h, Direction.RIGHT, hexes, visited)
    all_dirs += get_available_hexes_in_line_from(h, Direction.BOTTOM_RIGHT, hexes, visited)
    all_dirs += get_available_hexes_in_line_from(h, Direction.BOTTOM_LEFT, hexes, visited)
    all_dirs += get_available_hexes_in_line_from(h, Direction.LEFT, hexes, visited)
    return all_dirs


def get_one_distance_hexes(h, hexes, visited):
    for d in list(Direction):
        if h.has_neighbour(d):
            n = hexes[h.get_neighbour(d)]
            if not n.has_piece() and not has_visited(n, visited):
                visited.append(n.get_id())
    return visited


def remove_moves_ending_in_enemy_territory(h, hexes, visited):
    to_remove = []
    for v_id in visited:
        v = hexes[v_id]
        if v.has_owner():
            owner = v.get_owner()
            myself = h.get_piece()
            if not myself == owner and not owner == get_opponent(myself):
                to_remove.append(h.get_id())
    return [item for item in visited if item not in to_remove]


def get_moves_hex(h, hexes):

    possible = [h.get_id()]
    visited = [h.get_id()]

    # Temporarily remove piece (mimicking that piece "moves" when jumping)
    piece = h.get_piece()
    h.set_piece(0)

    while len(possible) > 0:
        possible = get_available_hexes_in_all_directions_from(h, hexes, visited)
        visited += possible

    visited.remove(h.get_id())
    visited = get_one_distance_hexes(h, hexes, visited)
    visited = remove_moves_ending_in_enemy_territory(h, hexes, visited)

    h.set_piece(piece)

    return visited


def get_possible_moves(hexes):
    possible_hex = []
    for h in hexes:
        ph = get_moves_hex(h, hexes)
        possible_hex.append(ph)
        print(h.get_id(), ph)
    return possible_hex
