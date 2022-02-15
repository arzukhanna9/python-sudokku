""" Test sudoku using Hypothesis. """

import string

from hypothesis import given
from hypothesis.strategies import lists, sampled_from, sets

from lib import sudoku

VALID_SUDOKU_VALUES = list(range(1, 10))
INVALID_SUDOKU_LETTERS = list(string.ascii_letters) + VALID_SUDOKU_VALUES
INVALID_SUDOKU_INTEGERS = list(range(10, 100)) + VALID_SUDOKU_VALUES


@given(sets(sampled_from(VALID_SUDOKU_VALUES), min_size=9, max_size=9))
def test_has_correct_cells(row):
    "Row has no letters or incorrect integers"
    assert sudoku.no_letters(row) and sudoku.no_wrong_integers(row)


@given(sets(sampled_from(VALID_SUDOKU_VALUES), min_size=9, max_size=9))
def test_has_no_letters(row):
    """Row has no duplicates."""
    assert sudoku.no_duplicates(row)


@given(sets(sampled_from(VALID_SUDOKU_VALUES), min_size=9, max_size=9))
def test_has_no_duplicates(row):
    """Row has no duplicates."""
    assert sudoku.no_duplicates(row)


@given(lists(sampled_from(VALID_SUDOKU_VALUES), min_size=10, max_size=10))
def test_has_duplicates(row):
    """Row has duplicates."""
    assert not sudoku.no_duplicates(row)


@given(sets(sampled_from(INVALID_SUDOKU_LETTERS), min_size=9, max_size=9))
def test_has_letter(row):
    """Row has a letter."""
    assert not sudoku.no_letters(row)


@given(sets(sampled_from(INVALID_SUDOKU_INTEGERS), min_size=9, max_size=9))
def test_has_incorrect_integer(row):
    """Row has integer outside range."""
    assert not sudoku.no_wrong_integers(row)
