"""
Unit tests to check functioning of Sudoku solver.
"""

from lib import sudoku

BLOCK = [[0, 2, 3], [4, 5, 6], [7, 8, 9]]

GOOD_LIST = [0, 2, 3, 4, 5, 6, 7, 8, 9]
INCORRECT_DIMENSION_LIST = [0, 2, 3, 4, 5, 6, 7, 8]
BAD_HAS_DUPLICATES = [6, 5, 4, 1, 9, 8, 3, 7, 6]
BAD_HAS_LETTER = [0, 1, 2, "a", 8, 9, 0, 0, 0, 0]
BAD_INTEGER_OUTSIDE_RANGE = [0, 1, 2, 10, 8, 9, 0, 0, 0, 0]


GOOD_GRID = [
    [0, 2, 0, 3, 5, 0, 0, 8, 4],
    [0, 0, 0, 4, 6, 0, 0, 5, 7],
    [0, 0, 0, 2, 0, 7, 0, 1, 0],
    [0, 0, 5, 0, 4, 0, 8, 0, 2],
    [0, 6, 9, 0, 2, 8, 0, 0, 0],
    [0, 0, 8, 0, 0, 0, 1, 0, 6],
    [7, 3, 0, 8, 0, 5, 4, 2, 0],
    [9, 0, 0, 7, 3, 0, 0, 6, 1],
    [0, 5, 0, 0, 9, 2, 0, 0, 8],
]

BAD_ROW_GRID = [
    [0, 2, 0, 3, 5, 0, 0, 8, 8],
    [0, 0, 0, 4, 6, 0, 0, 5, 7],
    [0, 0, 0, 2, 0, 7, 0, 1, 0],
    [0, 0, 5, 0, 4, 0, 8, 0, 2],
    [0, 6, 9, 0, 2, 8, 0, 0, 0],
    [0, 0, 8, 0, 0, 0, 1, 0, 6],
    [7, 3, 0, 8, 0, 5, 4, 2, 0],
    [9, 0, 0, 7, 3, 0, 0, 6, 1],
    [0, 5, 0, 0, 9, 2, 0, 0, 0],
]

BAD_COLUMN_GRID = [
    [0, 2, 0, 3, 5, 0, 0, 0, 8],
    [0, 0, 0, 4, 6, 0, 0, 5, 7],
    [0, 0, 0, 2, 0, 7, 0, 1, 0],
    [0, 0, 5, 0, 4, 0, 8, 0, 2],
    [0, 6, 9, 0, 2, 8, 0, 0, 0],
    [0, 0, 8, 0, 0, 0, 1, 0, 6],
    [7, 3, 0, 8, 0, 5, 4, 2, 0],
    [9, 0, 0, 7, 3, 0, 0, 6, 1],
    [0, 5, 0, 0, 9, 2, 0, 0, 8],
]

SOLVED_GRID = [
    [6, 2, 7, 3, 5, 1, 9, 8, 4],
    [8, 1, 3, 4, 6, 9, 2, 5, 7],
    [5, 9, 4, 2, 8, 7, 6, 1, 3],
    [1, 7, 5, 9, 4, 6, 8, 3, 2],
    [3, 6, 9, 1, 2, 8, 7, 4, 5],
    [2, 4, 8, 5, 7, 3, 1, 9, 6],
    [7, 3, 6, 8, 1, 5, 4, 2, 9],
    [9, 8, 2, 7, 3, 4, 5, 6, 1],
    [4, 5, 1, 6, 9, 2, 3, 7, 8],
]


def test_read_grid_text():
    """test if grid read in correctly from text file"""
    with open("data/easy.txt", "r") as text_file:
        grid_from_text = sudoku.read_grid(text_file)
    assert grid_from_text == GOOD_GRID


def test_read_grid_json():
    """test if grid read in correctly from json file"""
    with open("data/easy.json", "r") as json_file:
        grid_from_json = sudoku.read_grid(json_file)
    assert grid_from_json == GOOD_GRID


def test_read_grid_file_invalid():
    """test output when file type invalid"""
    with open("data/invalid_file", "r") as invalid_file:
        grid_from_invalid = sudoku.read_grid(invalid_file)
    assert grid_from_invalid is None


def test_same_grid_with_text_and_json():
    """get same grid when input is text and json"""
    with open("data/easy.txt", "r") as text_file:
        grid_from_text = sudoku.read_text_file(text_file)
    with open("data/easy.json", "r") as json_file:
        grid_from_json = sudoku.read_json_file(json_file)
    assert grid_from_text == grid_from_json


def test_grid_dimension_is_valid():
    """Dimensions valid"""
    assert sudoku.is_dimension_valid(GOOD_LIST)


def test_grid_dimension_is_invalid():
    """Dimensions invalid"""
    assert not sudoku.is_dimension_valid(INCORRECT_DIMENSION_LIST)


def test_grid_list_valid():
    """Rows and columns valid"""
    assert sudoku.is_row_valid(GOOD_LIST)
    assert sudoku.is_column_valid(GOOD_LIST)


def test_grid_list_invalid():
    """Rows and columns valid"""
    assert not sudoku.is_row_valid(BAD_INTEGER_OUTSIDE_RANGE)
    assert not sudoku.is_column_valid(BAD_INTEGER_OUTSIDE_RANGE)


def test_grid_list_duplicates_invalid():
    """Row/Column has duplicates - invalid"""
    assert not sudoku.no_duplicates(BAD_HAS_DUPLICATES)


def test_grid_list_cell_letter_invalid():
    """Row/Column has a letter - invalid"""
    assert not sudoku.no_letters(BAD_HAS_LETTER)


def test_grid_list_cell_outside_range_invalid():
    """Row/Column has a cell outside the range - invalid"""
    assert not sudoku.no_wrong_integers(BAD_INTEGER_OUTSIDE_RANGE)


def test_is_grid_valid():
    """Entire grid is valid"""
    assert sudoku.is_grid_valid(GOOD_GRID)


def test_is_grid_row_invalid():
    """Grid has invalid row"""
    assert not sudoku.is_grid_valid(BAD_ROW_GRID)


def test_is_grid_column_invalid():
    """Grid has invalid row"""
    assert not sudoku.is_grid_valid(BAD_COLUMN_GRID)


def test_move_possible_in_list():
    """n is a possible move in the empty cell"""
    assert sudoku.can_move(GOOD_LIST, 1)


def test_move_not_possible_in_list():
    """n is not a possible move in the empty cell"""
    assert not sudoku.can_move(GOOD_LIST, 2)


def test_block_to_list():
    """Can convert 3x3 cell to list"""
    assert sudoku.convert_block_to_list(BLOCK, 0, 0) == GOOD_LIST


def test_next_empty_correct():
    """return next empty cell"""
    assert sudoku.next_empty(GOOD_GRID) == (0, 0)


def test_next_empty_incorrect():
    """return next empty cell"""
    assert sudoku.next_empty(GOOD_GRID) != (0, 3)


def test_next_empty_none():
    """return next empty cell"""
    assert sudoku.next_empty(SOLVED_GRID) == (None, None)


def test_possible_move():
    """is a possible move"""
    assert sudoku.possible(GOOD_GRID, 0, 0, 6)


def test_not_possible_move():
    """is not aa possible move"""
    assert not sudoku.possible(GOOD_GRID, 0, 0, 2)


def test_puzzle_solved_correctly():
    """puzzle can be solved correctly"""
    assert sudoku.solve_puzzle(GOOD_GRID)
