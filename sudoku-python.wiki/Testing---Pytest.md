## Unit Testing

Known values are tested to known responses.The unit tests have been designed in a 
way to test the functionality of each small component of the program. Specifically, 
they test how the program handles both incorrect and correct inputs. Specific lists 
have been created to be tested by the test functions which all begin with `test_`

Example:
```python
GOOD_LIST = [1, 2, 3, 4, 5, 6, 7, 8, 9]
LIST_WITH_DUPLICATES = [6, 5, 4, 1, 9, 8, 3, 7, 6]

def test_grid_list_valid():
    """Rows and columns valid"""
    assert sudoku.is_row_valid(GOOD_LIST)
    assert sudoku.is_column_valid(GOOD_LIST)


def test_grid_list_duplicates_invalid():
    """Row/Column has duplicates - invalid"""
    assert not sudoku.no_duplicates(LIST_WITH_DUPLICATES)
    assert not sudoku.no_duplicates(LIST_WITH_DUPLICATES)
```