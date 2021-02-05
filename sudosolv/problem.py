from search import Problem
from board import SudokuBoard, SudokuBoardSmart


class SudokuProblemClass(Problem):

    def __init__(self, filled_initial_cells):
        """ Constructor: filled_initial_cells is a dictionary
                        specifying which cells are already filled.
        """
        super().__init__(SudokuBoard(filled_initial_cells))

    def actions(self, state):
        # Define all possible actions from the given state.
        if not state.is_valid():
            return []  # no actions
        return state.get_possible_fills()

    def result(self, state, action):
        (i, j, k) = action
        return state.fill_up(i, j, k)

    def goal_test(self, state):
        return state.goal_test()

    def path_cost(self, c, state1, action, state2):
        return 1


class SudokuProblemClassSmart(Problem):

    # Note:
    # A state of the sudoku problem is given by a dictionary
    #  mapping coordinate (i,j) -> k
    #  in other words, at (i, j) we have the number k where
    #   1 <= i <= 9, 1 <= j <= 9 and k is between 1 and 9
    # If a coordinate has no number in it, it is simply omitted from
    # the dictionary.

    def __init__(self, filled_initial_cells):
        """ Constructor: filled_initial_cells is a dictionary
                        specifying which cells are already filled.
        """
        super().__init__(SudokuBoardSmart(filled_initial_cells))

    def actions(self, state):
        # Define all possible actions from the given state.
        if not state.is_valid():
            return []  # no actions
        return state.get_possible_fills()

    def result(self, state, action):
        (i, j, k) = action
        return state.fill_up(i, j, k)

    def goal_test(self, state):
        return state.goal_test()

    def path_cost(self, c, state1, action, state2):
        return 1
