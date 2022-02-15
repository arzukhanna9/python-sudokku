A type of property-based testing that verifies the program code using a large 
range of relevant inputs. To use this, a list of valid and invalid inputs need to 
be declared and stored in a variable from which the hypothesis tests generate a 
random sample to test correctness of code.

`@given` is a decorator that takes a test function and turns it into a parametrized one which, 
when called, runs the test over a wide range data matching the specified data type.
* `sets` ensures that only one of each value in the specified range is used to 
generate the random test.
  
* `sampled_from` specifies the list from which the values are randomly being chosen 
from (initialised beforehand).

Example:
```python
VALID_SUDOKU_VALUES = list(range(1, 10))

@given(sets(sampled_from(VALID_SUDOKU_VALUES), min_size=9, max_size=9))
def test_has_correct_cells(row):
    "Row has no letters or incorrect integers"
    assert sudoku.no_letters(row) and sudoku.no_wrong_integers(row)
```