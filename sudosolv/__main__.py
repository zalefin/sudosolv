from problem import SudokuProblemClassSmart
from search_algorithms import iterative_deepening_search
from sudosolv import string2state


if __name__ == "__main__":
    # s = """*******69
# **269****
# *5***1**3
# 5*1**6***
# ***8*5***
# ***3**8*7
# 6**5***2*
# ****645**
# 71*******"""
    s = """**25****1
***6****3
1*9***57*
***1*69**
**6***7**
**72*4***
*54***3*7
3****9***
2****54**"""
    state = string2state(s)
    sudoku = SudokuProblemClassSmart(state)
    sudoku.initial.pretty_print()
    result = iterative_deepening_search(sudoku)
    print(result)
    print('Done !!!')
    print('Soln:')
    result.state.pretty_print()
