## Input

A text or JSON file with a grid representing the sudoku puzzle to be solved.

### Grid

A valid grid is one that:

* Contains a total of 81 integers in a 9x9 grid format
* Integers represent a cell and must be in range `0` to `9`
    * `0` - represents an empty cell that needs to be solved
    * `1` to `9` - are cells that have been solved and must not change
* Each row of the grid starts on a new line
* There are no duplicate integers in any row, column or 3x3 cell

#### Example Easy Puzzle

Source (text): [data/easy.txt](data/easy.txt)

```text
0 2 0 3 5 0 0 8 4
0 0 0 4 6 0 0 5 7
0 0 0 2 0 7 0 1 0
0 0 5 0 4 0 8 0 2
0 6 9 0 2 8 0 0 0
0 0 8 0 0 0 1 0 6
7 3 0 8 0 5 4 2 0
9 0 0 7 3 0 0 6 1
0 5 0 0 9 2 0 0 8
```

Source (json): [data/easy.json](data/easy.json)

```json
{
  "puzzle":
    [[0, 2, 0, 3, 5, 0, 0, 8, 4],
    [0, 0, 0, 4, 6, 0, 0, 5, 7],
    [0, 0, 0, 2, 0, 7, 0, 1, 0],
    [0, 0, 5, 0, 4, 0, 8, 0, 2],
    [0, 6, 9, 0, 2, 8, 0, 0, 0],
    [0, 0, 8, 0, 0, 0, 1, 0, 6],
    [7, 3, 0, 8, 0, 5, 4, 2, 0],
    [9, 0, 0, 7, 3, 0, 0, 6, 1],
    [0, 5, 0, 0, 9, 2, 0, 0, 8]]
}
```

## Output

Solved sudoku puzzles with same dimensions as input with all `0`'s replaced with integers in 
range from `1` to `9`. 

NOTE: Output solution and format is the same for both text and json input files.

#### Example Solved Puzzle

```bash
python3 solve_sudoku.py data/easy.txt

[[6 2 7 3 5 1 9 8 4]
 [8 1 3 4 6 9 2 5 7]
 [5 9 4 2 8 7 6 1 3]
 [1 7 5 9 4 6 8 3 2]
 [3 6 9 1 2 8 7 4 5]
 [2 4 8 5 7 3 1 9 6]
 [7 3 6 8 1 5 4 2 9]
 [9 8 2 7 3 4 5 6 1]
 [4 5 1 6 9 2 3 7 8]]
 ```

#### Example output when wrong file type given

Source: [data/invalid_file](data/invalid_file)

A log error is returned in the format below.

```bash
    $ python3 solve_sudoku.py data/invalid_file
    
    2021-07-16 09:10:16,535:ERROR:Cannot read file type None
```