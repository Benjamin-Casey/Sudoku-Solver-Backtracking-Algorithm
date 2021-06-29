# Sudoku Solver (Backtracking Algorithm)

This script takes a sudoku board and uses a backtracking algorithm to solve it.

## How it works

The main solve loop utilises a recursive function. The function cycles trhough the numbers 1-9 to try to find an eligible number for the unsolved square that it is dealing with. If an eligible number is found, the program recurs itself to deal with the next unsolved number.

If no elgible number can be found, the recurred function pops off the call stack, and the previous iteration of the function repeats, iterating through numbers 1-9 until an eligible nubmer is found, and then recurring.

Essentially, the algorithm enters a number assuming it's right, and continues. If the puzzle can't be solved this way, it goes back, changes the number, and tries something else. 