from io import StringIO
from problem import SudokuProblemClassSmart
from search_algorithms import iterative_deepening_search


def string2state(s):
    state = {}
    with StringIO(s) as file:
        row_id = 1
        for rows in file:
            rows = rows.strip()
            cont_list = [char for char in rows]
            for (col_id, row_contents) in enumerate(cont_list):
                row_contents = row_contents.strip()
                if '1' <= row_contents <= '9':
                    state[(row_id, col_id + 1)] = int(row_contents)
            row_id = row_id + 1
        file.close()
    return state


def run_solver(init_state: dict, search_algo=iterative_deepening_search, verbose=False):
    sudoku = SudokuProblemClassSmart(init_state)
    if verbose: sudoku.initial.pretty_print()
    result = search_algo(sudoku)
    if verbose:
        print('Done!')
        if result:
            print('Soln:')
            result.state.pretty_print()
        else:
            print('No soln found.')
    return result
