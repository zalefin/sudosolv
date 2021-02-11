# sudosolv - Sudoku Solver

The solver works by implementing two fill strategies, "implied fill" and "number scan fill" and toggling between them.
Each time a node is initialized, implied fill is first applied. Then number scan fill is applied.
This repeats indefinitely until either the `has_conflict` flag is set True or both strategies
return no valid fills back-to-back, at which point it recurses.

The "number scan fill" strategy works by "squeezing" numbers into a hole.
It loops over every 3x3 block on the board, loops over every unfilled cell in that
block, picks an unfilled number in that block, and checks if the selected position is
the only valid position for that number by flagging all other blocks in the cell as either
filled or having conflicts / being invalid.

This strategy seems to be faster in cases where there are a lot of "aligned" values, but
causes the run time to be much worse when there are not, and a lot of recursion is
required to establish many "aligned" values.

Similarly to using no fill strategies, in the worst case, the tree depth is equal
to the number of unfilled cells at the start. The branching factor is 9.

## Requires
- Python3

## Running
The solver can be executed by running `python sudosolv [BOARD FILE]`
