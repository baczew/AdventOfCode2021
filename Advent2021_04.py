def tic_tac(func):

    import time
    def inner(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        exec_time = end_time - start_time
        print(f'Execution took: {exec_time}')
        return result
    return inner


class Board():

    n_col = 5
    n_row = 5

    def __init__(self):
        self._contents = list()
        self._found_numbers = list([Board.n_col * 0] * Board.n_row)
        self._won = False

    @property
    def won(self):
        return self.check_winning()

    @property
    def contents(self):
        return self._contents

    @contents.setter
    def contents(self, row):
        if len(self._contents) < Board.n_row and len(row) == Board.n_col:
            self._contents.append(row)

    @contents.deleter
    def contents(self):
        self._contents = []

    def check_if_contains(self, number, mark = False):
        if any(number in x for x in self.contents):
            for row_index, row_contents in enumerate(self.contents):
                if number in row_contents:
                    for column_index, column_contents in enumerate(row_contents):
                        if column_contents == number:
                            if mark:
                                self.mark_position(row_index, column_index)
                            return row_index, column_index

    def mark_position(self, r, c):
        self._contents[r][c] = 'X'

    def check_winning(self):
        import numpy as np
        if ['X'] * Board.n_col in self.contents:
            #print("Won (row)")
            #print(self.contents)
            return True
        if ['X'] * Board.n_row in np.transpose(self.contents).tolist():
            #print("Won (column)")
            #print(self.contents)
            return True
        else:
            return False

def load_data(file):

    with open(file) as op:

        input_list_strings = op.read().split('\n')[:-1]

    return input_list_strings

@tic_tac
def lets_play_bingo(boards, numbers, which_wins):

    n_won = 0

    for i in numbers:
        for j in [b for b in boards if not b.won]:
            j.check_if_contains(i, mark = True)
            if j.check_winning():
                n_won += 1
                if n_won == which_wins:
                    return i * sum([sum([z for z in y if z != 'X']) for y in j.contents])

def prepare_boards(data_input):

    list_of_boards = []
    example = Board()
    for n, row in enumerate(data_input[2:]):

        if len(row) == 0:
            list_of_boards.append(example)
            example = Board()

        else:
            row_list = [int(i) for i in row.split(' ') if len(i) > 0]
            example.contents = row_list

    return list_of_boards


def main():

    data = load_data('Files/input4.txt')
    random_numbers = list(map(int, data[0].split(',')))

    list_of_boards1 = prepare_boards(data)
    list_of_boards2 = prepare_boards(data)


    result1 = lets_play_bingo(list_of_boards1, random_numbers, 1)
    print('Result of 1st part: ', result1)

    result2 = lets_play_bingo(list_of_boards2, random_numbers, len(list_of_boards2))
    print('Result of 2st part: ', result2)


if __name__ == "__main__":
    main()








