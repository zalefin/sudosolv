

class SudokuBoard:

    # The class SudokuBoard has a single field
    #  self.contents : A dictionary from (i,j) -> k
    #     the dictionary indicates that cell (i,j) has number k
    #     Empty cells are not present in the self.contents field.
    # Constructor: DO NOT MODIFY
    def __init__(self, filled_cells_dict):
        self.contents = filled_cells_dict

    # A pretty printer that will come in handy later
    # This will print the sudoku board in a nice readable format.
    # DO NOT MODIFY
    def pretty_print(self):
        state = self.contents
        # Iterate through each row
        blk_sep = '|' + '-' * 9 + '+' + '-' * 9 + '+' + '-' * 9 + '|'
        print(blk_sep)
        for row_id in range(1, 10):
            # Iterate through each column
            row_str = '|'
            for col_id in range(1, 10):
                # If row is not empty
                if (row_id, col_id) in state:
                    row_str = row_str + ' ' + \
                        str(state[(row_id, col_id)]) + ' '
                else:
                    row_str = row_str + '   '
                if col_id % 3 == 0:
                    row_str = row_str + '|'
            print(row_str)
            if row_id % 3 == 0:
                print(blk_sep)

    # Function: get_numbers_for_row
    # Return a list of all the numbers tha are currently
    # in row number j. Where 1 <= j <= 9
    # DO NOT MODIFY
    def get_numbers_for_row(self, j):
        assert(j >= 1 and j <= 9)
        state = self.contents
        row_nums = [state[(j, k)]
                    for k in range(1, 10)
                    if (j, k) in state.keys()]
        return row_nums

    # Function: get_numbers_for_col
    # Return a list of all the numbers that are currently
    # in column number j. Where 1 <= j <= 9
    # DO NOT MODIFY
    def get_numbers_for_col(self, j):
        assert(j >= 1 and j <= 9)
        state = self.contents
        col_nums = [state[(k, j)]
                    for k in range(1, 10)
                    if (k, j) in state.keys()]
        return col_nums

    # Function: get_numbers_for_block
    # Return a list of all the numbers that are currently
    # in the block blk_x, blk_y
    # DO NOT MODIFY
    def get_numbers_for_block(self, blk_x, blk_y):
        assert(1 <= blk_x <= 3)
        assert(1 <= blk_y <= 3)
        state = self.contents
        row_nums = [state[(j, k)]
                    for j in range(blk_x * 3 - 2, blk_x * 3 + 1)
                    for k in range(blk_y * 3 - 2, blk_y * 3 + 1)
                    if (j, k) in state.keys()]
        return row_nums

    def get_cells_for_block(self, blk_x, blk_y):
        assert(1 <= blk_x <= 3)
        assert(1 <= blk_y <= 3)
        cells = [(i, j)
                 for i in range(blk_x * 3 - 2, blk_x * 3 + 1)
                 for j in range(blk_y * 3 - 2, blk_y * 3 + 1)]
        return cells

    # Function: has_repeated_entries
    # Check if a list of numbers has at least one number
    # that repeats (more than once).
    # return False if all elements are unique
    # return True if some element is repeated
    # DO NOT MODIFY

    def has_repeated_entries(self, lst_of_numbers):
        if len(lst_of_numbers) == len(set(lst_of_numbers)):
            return False
        else:
            return True

    # Function: is_valid
    # Write a function that checks that
    #  - Each row/column/block has no more than one
    #      occurrence of number 1 - 9
    #  - We have a flag called verbose that you can
    #      use to print a message if you wish or simply ignore it.
    #    Our test cases will be calling with verbose = True
    #    that way you can see what is happening/debug better
    #    if you place print statements protected by if (verbose)
    #    But the search will call with verbose = False.
    #  Return TRUE if no repetition is seen in the board.
    #  Return FALSE if a number has repeated in row, column or block.
    def is_valid(self, verbose=False):
        # Use the functions
        #  self.get_numbers_for_row
        #  self.get_numbers_for_col
        #  self.get_numbers_for_block
        #  self.has_repeated_entries
        for i in range(1, 10):
            if self.has_repeated_entries(self.get_numbers_for_row(i)):
                return False
        for j in range(1, 10):
            if self.has_repeated_entries(self.get_numbers_for_col(j)):
                return False
        for blkx in range(1, 4):
            for blky in range(1, 4):
                if self.has_repeated_entries(
                        self.get_numbers_for_block(blkx, blky)):
                    return False
        return True

    # Function: get_block_number
    # Useful function to find out which block (i,j) belongs to.
    # DO NOT MODIFY
    def get_block_number(self, i, j):
        return ((i - 1) // 3 + 1, (j - 1) // 3 + 1)

    # Function: get_possible_fills
    # Return a list (i, j, k) of all possible "fills"
    #   I.e, we can fill cell (i,j) with number k
    # Note that for same cell (i,j) there are many possible ks that can
    # be filled. Each such possibility will have a separate
    #  (i,j,k) entry.
    #
    #   (a) You must ensure that (i,j) is not filled in the current board.
    #   (b) You must ensure that k does not occur elsewhere in
    #      - row i
    #      - column j
    #      - 3x3 block in which (i,j) is located.
    #      Useful functions:
    #        self.get_block_number
    #        self.get_numbers_for_row
    #        self.get_numbers_for_col
    #        self.get_numbers_for_block
    # This function
    def get_possible_fills(self):
        # state is a dictionary mapping (x,y) cell coordinate to number
        state = self.contents
        # First get a list of cells that are not filled
        lst_of_unfilled_cells = [(i, j)
                                 for i in range(1, 10)
                                 for j in range(1, 10)
                                 if (i, j) not in state.keys()]

        # 2. For each unfilled cell get all the valid_actions for that cell
        valid_actions = []  # add (i,j,k) to valid_actions
        #   if (i,j) isunfilled and k is a number between 1 to 9
        #   and k does not occur in row i, column j, or block corr. to (i,j)
        for (i, j) in lst_of_unfilled_cells:
            for k in range(1, 10):
                if self.fill_up(i, j, k).is_valid():
                    valid_actions.append((i, j, k))
        return valid_actions

    # Function: fill_up
    # fill up cell (i,j) with k
    # return a new Board with same as current board
    #  but cell (i,j) has number k.
    # DO NOT MODIFY
    def fill_up(self, i, j, k):
        assert((i, j) not in self.contents.keys())
        # Let us copy the dictionary over.
        new_state = self.contents.copy()
        assert (1 <= i <= 9 and 1 <= j <= 9 and 1 <= k <= 9)
        # Assign cell (i,j) to number k
        new_state[(i, j)] = k
        # Return a SudokuBoard structure
        return SudokuBoard(new_state)

    # Function: goal_test
    #  Check if the current board has been fully filled
    #  and in a valid manner.
    def goal_test(self):
        state = self.contents
        if not self.is_valid():
            return False
        # Check that all the cells are filled
        # I.e, for each i in 1..9 and for each j in 1..9,
        #      check that (i,j) is in the dictionary
        #      check that state[(i,j)] is between 1 and 9
        # The rest of the task is already achieved by call to is_valid above.
        if len(state.keys()) != 81:
            return False
        for cell in state.values():
            if cell not in range(1, 10):
                return False
        return True

    # Define a hash function
    # This is for the search algorithms later.
    # do not modify.
    def __hash__(self):
        cells_lst = [(i, j, k) for ((i, j), k) in self.contents.items()]
        return hash(frozenset(cells_lst))


class SudokuBoardSmart(SudokuBoard):

    def __init__(self, filled_cells_dict, do_smart_fills=True):
        super().__init__(filled_cells_dict)
        self.has_conflict = False
        if do_smart_fills:
            self.do_all_smart_fills(False)

    def get_block_number(self, i, j):
        return ((i - 1) // 3 + 1, (j - 1) // 3 + 1)

    def find_implied_fills(self, verbose=False):
        # This function should return a list
        #     [(i,j,k) s.t. k is the only possible fill for (i,j)]
        # As described in the writeup above, if it finds a conflict,
        #  then it must set the flag self.has_conflict = True
        #  In the case of conflict you may just return the empty list.
        # Any debug messages you print must first check if verbose flag
        # is set to true.
        # Or you can just ignore the verbose flag,
        # and not print anything from the function.

        state = self.contents  # dictionary representing the board
        implied_fill_list = []  # initialize the list we will return
        # find all cells that are not filled yet
        unfilled_cells = [(i, j)
                          for i in range(1, 10)
                          for j in range(1, 10)
                          if (i, j) not in state.keys()]
        # for each unfilled cell,
        #    compute list of possible fills
        #    if list is a singleton, then append it to implied_fill_list
        #    if list is empty, set has_conflict to True (and return the empty list)
        # return implied_fill_list
        for i, j in unfilled_cells:
            blk_nums = self.get_numbers_for_block(*self.get_block_number(i, j))
            row_nums = self.get_numbers_for_row(i)
            col_nums = self.get_numbers_for_col(j)
            diff = list(set(range(1, 10)) -
                        set(blk_nums + row_nums + col_nums))

            if len(diff) == 0:
                self.has_conflict = True
                return []

            if len(diff) == 1:
                k = diff[0]
                implied_fill_list.append((i, j, k))

        return implied_fill_list

    # black magic
    def adj_channels(self, x):
        return (((x) % 3) + 3 * ((x - 1) // 3) + 1, ((x + 1) % 3) + 3 * ((x - 1) // 3) + 1)

    # def adj_cells_in_block(self, i_in, j_in):
    #     # move into standard block 0 indexed
    #     i = (i_in - 1) % 3
    #     j = (j_in - 1) % 3
    #     out_diffs = []
    #     if i > 0: out_diffs.append((-1, 0))
    #     if i < 2: out_diffs.append((1, 0))
    #     if j > 0: out_diffs.append((0, -1))
    #     if j < 2: out_diffs.append((0, 1))
    #     return out_diffs

    def find_number_scan_fills(self, verbose=False):
        state = self.contents
        num_scan_fills_list = []

        # block loop
        for blk_x in range(1, 4):
            for blk_y in range(1, 4):
                in_blk_cells = self.get_cells_for_block(blk_x, blk_y)
                unfilled_in_blk_cells = [(j, k)
                                         for j, k in in_blk_cells
                                         if (j, k) not in state.keys()]
                blk_nums = self.get_numbers_for_block(blk_x, blk_y)
                diff = list(set(range(1, 10)) - set(blk_nums))
                for (i, j) in unfilled_in_blk_cells:
                    for k in diff:
                        # check 4 channels
                        ia1, ia2 = self.adj_channels(i)
                        ja1, ja2 = self.adj_channels(j)

                        death = []
                        # paint beams
                        if k in self.get_numbers_for_row(ia1):
                            death += [(p, q) for p, q in in_blk_cells if p == ia1]
                        if k in self.get_numbers_for_row(ia2):
                            death += [(p, q) for p, q in in_blk_cells if p == ia2]
                        if k in self.get_numbers_for_col(ja1):
                            death += [(p, q) for p, q in in_blk_cells if q == ja1]
                        if k in self.get_numbers_for_col(ja2):
                            death += [(p, q) for p, q in in_blk_cells if q == ja2]
                        death += [(p, q) for p, q in in_blk_cells if (p, q) in state.keys()]

                        # ich1 = k in self.get_numbers_for_row(ia1)
                        # ich2 = k in self.get_numbers_for_row(ia2)
                        # jch1 = k in self.get_numbers_for_col(ja1)
                        # jch2 = k in self.get_numbers_for_col(ja2)
                        # ifil1 = (ia1, j) in state.keys()
                        # ifil2 = (ia2, j) in state.keys()
                        # jfil1 = (i, ja1) in state.keys()
                        # jfil2 = (i, ja2) in state.keys()
                        # if (ich1 or jfil1) and (ich2 or jfil2) and (jch1 or ifil1) and (jch2 or ifil2):
                        # TODO add check remain invalid optimization
                        if len(set(death)) == 8:
                        # if ich1 and ich2 and jch1 and jch2:
                            # print('up {}, right {}, down {}, left{}, pos {}'.format((ia1, j), (i, ja1), (ia2, j), (i, ja2), (i,j)))
                            row_collide = k in self.get_numbers_for_row(i)
                            col_collide = k in self.get_numbers_for_col(j)
                            if not (row_collide or col_collide):
                                # self.pretty_print()
                                # print(self.is_valid())
                                num_scan_fills_list.append((i, j, k))

        return num_scan_fills_list

#                     row_nums = self.get_numbers_for_row(i)
#                     col_nums = self.get_numbers_for_col(j)
#                     diff = list(set(range(1, 10)) -
#                                 set(blk_nums + row_nums + col_nums))

#                     if len(diff) == 0:
#                         self.has_conflict = True
#                         return []

#                     if len(diff) == 1:
#                         k = diff[0]
#                         implied_fill_list.append((i, j, k))

    # Function: do_all_implied_fills
    # repeatedly find implied fills and perform them.
    # keep finding new implied fills until no more are left.
    # DO NOT MODIFY
    def do_all_smart_fills(self, verbose=False):
        # done = False
        # state = self.contents
        # while (not done and not self.has_conflict):
        #     lst = self.find_implied_fills(verbose)
        #     if len(lst) == 0:
        #         done = True
        #     else:
        #         for (i, j, k) in lst:
        #             state[(i, j)] = k
        # return
        state = self.contents
        quit = 0
        mode = 0
        while (quit < 2 and not self.has_conflict):
            if mode == 0:
                lst = self.find_implied_fills(verbose)
            elif mode == 1:
                lst = self.find_number_scan_fills(verbose)

            if len(lst) == 0:
                quit += 1
                # quit = 2
            else:
                quit = 0
                for i, j, k in lst:
                    state[(i, j)] = k
            mode = (mode + 1) % 2

    def is_valid(self, verbose=False):
        return not(self.has_conflict) and super().is_valid(verbose)

    def fill_up(self, i, j, k):
        # fill up cell (i,j) with k
        # return a new Board
        new_state = self.contents.copy()
        assert (1 <= i <= 9 and 1 <= j <= 9 and 1 <= k <= 9)
        new_state[(i, j)] = k
        return SudokuBoardSmart(new_state)
