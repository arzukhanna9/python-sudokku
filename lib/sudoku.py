"""
Library program to solve Sudoku puzzles.
Author: Arzu Khanna
"""
import json
import logging
import mimetypes

import _io

log = logging.getLogger()


def read_grid(file: _io.TextIOWrapper) -> list:
    """
    Read grid data from file.
    :param file: Text or JSON file containing sudoku puzzle to be solved.
    :return: List of lists representing sudoku puzzle.
    """

    file_type, _ = mimetypes.guess_type(file.name)
    grid = None
    if file_type == "text/plain":
        grid = read_text_file(file)
    elif file_type == "application/json":
        grid = read_json_file(file)
    else:
        log.error("Cannot read file type %s", file_type)
    return grid


def read_text_file(file: _io.TextIOWrapper) -> list:
    """
    Read in a text file.
    :param file: Text file containing sudoku puzzle
    :return: List of lists representing sudoku puzzle.
    """
    log.debug("Reading in TEXT file %s", file.name)
    grid = []
    for line in file:
        grid.append([int(n) for n in line.split()])
    return grid


def read_json_file(file: _io.TextIOWrapper) -> list:
    """
    Read in a JSON file.
    :param file: JSON file containing sudoku puzzle
    :return: List of lists representing sudoku puzzle.
    """
    log.debug("Reading in JSON file %s", file.name)
    data = json.load(file)
    return data["puzzle"]


def is_dimension_valid(a_list: list) -> bool:
    """
    To have valid dimensions, the grid has to be a 2 dimensional array
    with 9 rows and 9 columns.
    :param a_list: List in sudoku puzzle
    :return: TRUE if dimensions are valid, FALSE otherwise.
    """
    return bool(len(a_list) == 9)


def no_duplicates(row: list) -> bool:
    """Check row has no duplicates.
    :param row: row in puzzle"""
    _row = [i for i in row if i != 0]
    duplicates = len(set(_row)) != len(_row)
    log.debug("No duplicates in row/column...%s", row)
    return not duplicates


def no_letters(row: list) -> bool:
    """Check does row have letter
    :param row: row in puzzle"""
    no_letter = all(isinstance(i, int) for i in row)
    log.debug("No letters in row/column...%s", row)
    return no_letter


def no_wrong_integers(row: list) -> bool:
    """Check does cell have integer out of correct range
    :param row: row in puzzle"""
    no_wrong_integer = all(0 <= i <= 9 for i in row)
    log.debug("No wrong integers in row/column...%s", row)
    return no_wrong_integer


def is_row_valid(row: list) -> bool:
    """
    For a row to be valid, it should not contain duplicates of integers
    other than 0 and all cell values should be valid (see is_cell_valid).
    :param row: Row in the sudoku puzzle.
    :return: TRUE if row is valid, FALSE otherwise.
    """
    valid = all(
        [
            no_duplicates(row),
            no_letters(row),
            no_wrong_integers(row),
            is_dimension_valid(row),
        ]
    )
    return valid


def is_column_valid(column: list) -> bool:
    """
    For a column to be valid, it should not contain duplicates of integers
    other than 0 and all cell values should be valid (see is_cell_valid).
    :param column: Column in the sudoku puzzle.
    :return: TRUE if column is valid, FALSE otherwise.
    """
    return is_row_valid(column)


def is_grid_valid(grid: list) -> bool:
    """
    The grid is valid if it satisfies all other functions ending in _is_valid.
    :param grid: List of lists representing sudoku puzzle.
    :return: TRUE if grid is valid, FALSE otherwise.
    """
    for row in grid:
        if not is_row_valid(row):
            log.debug("Row dimensions are invalid...%s", row)
            return False

    transposed_grid = map(list, zip(*grid))
    for column in transposed_grid:
        if not is_column_valid(column):
            log.debug("Column dimensions are invalid...%s", column)
            return False

    log.debug("Entire grid is valid!")
    return True


def can_move(puzzle_list: list, _n: int) -> bool:
    """
    Determines whether _n can go in particular row/column/block.
    This is if _n doesn't already exist in the row/column/block.
    :param: list representing a row, column or block in the puzzle
    """
    return _n not in puzzle_list


def convert_block_to_list(grid: list, _row: int, _col: int) -> list:
    """
    Converts a 3x3 block into a list format.
    :param grid: Current state of sudoku puzzle.
    :param _row: Row
    :param _col: Column
    :return: list representing numbers in the 3x3 block
    """
    block = []
    _col0 = (_col // 3) * 3
    _row0 = (_row // 3) * 3
    for i in range(3):
        for j in range(3):
            block.append(grid[_row0 + i][_col0 + j])
    return block


def possible(grid: list, _row: int, _col: int, _n: int) -> bool:
    """
    Function: Determines whether inputting n in a particular cell (grid[y][x])
    is possible according to sudoku rules.
    :param grid: Current state of sudoku puzzle.
    :param _row: Row
    :param _col: Column
    :param _n: Number in cell
    :return: TRUE if possible for n to go in cell, FALSE otherwise.
    """
    rows = grid[_row]
    transposed_grid = list(map(list, zip(*grid)))
    column = transposed_grid[_col]
    block = convert_block_to_list(grid, _row, _col)

    move = all([can_move(rows, _n), can_move(column, _n), can_move(block, _n)])
    if move:
        log.debug("Next move is %d in cell (%d, %d)", _n, _row, _col)
    return move


def next_empty(grid: list) -> (int, int):
    """
    Function: Iterates through the cells in the puzzle to find the
    next empty cell which needs to be solved.
    :param grid: current state of sudoku puzzle
    """
    for _row in range(9):
        for _col in range(9):
            if grid[_row][_col] == 0:
                return _row, _col
    log.debug("There are no more empty cells to fill!")
    return None, None


def solve_puzzle(grid: list) -> bool:
    """
    Function: Solve the sudoku puzzle
    :param grid: current state of sudoku puzzle
    """

    _row, _col = next_empty(grid)

    if _row is None:
        log.debug("Puzzle solved successfully!")
        return True

    for _n in range(1, 10):
        if possible(grid, _row, _col, _n):
            grid[_row][_col] = _n
            if solve_puzzle(grid):
                return True

        grid[_row][_col] = 0

    return False
