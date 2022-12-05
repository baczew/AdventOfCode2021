import os
import numpy as np
import collections

def main():

    # Read data
    data, folds = load_data('/Users/Mateusz/Documents/Programowanie/Advent of Code/input13.txt')
   
    # Create a board
    game_board = Board()

    # Add data to the board
    for coordinates in data:
        y, x = coordinates
        game_board.enlarge_to_shape(x + 1, y + 1)
        game_board.set_value(x, y)
   
    # Fill so that is possible to fold the board
    game_board.fill()    

    # Make 1st fold
    axis, index = folds[0]
    game_board.fold(index, axis)

    # Count (part 1 answer)
    print(game_board.dots_count)
    
    #Make the rest of folds
    for fold in folds[1:]:
        axis, index = fold
        game_board.fold(index, axis)   

    # Print content (part 2 answer)
    print(game_board.content)
    


def load_data(file):

    input_list_of_lists = []
    input_folds = []

    with open(file) as op:

        for line in op.readlines():
            
            if line.startswith('fold'):
                
                fold_slicer = slice(11, -1)
                parameter_position = 1

                folds_tuple = line[fold_slicer].strip().split("=")
                folds_tuple[parameter_position] =  int(folds_tuple[parameter_position])

                input_folds.append(folds_tuple)

            elif line.strip():

                line_tuple_str = line[:-1].split(',')
                line_tuple_int = list(map(int, line_tuple_str))

                input_list_of_lists.append(line_tuple_int)

    return input_list_of_lists, input_folds


class Board():
    
    def __init__(self) -> None:
        self.content = np.matrix([0], dtype = np.int8)

    @property
    def shape(self):
        return self.content.shape

    @property
    def dots_count(self):
        return np.sum(self.content)

    def enlarge_to_shape(self, rows, columns):

        rows, columns = np.subtract((rows, columns), self.shape)
    
        if columns > 0:
            add = np.matrix([[0] * columns] * self.content.shape[0])
            self.content = np.hstack([self.content, add])

        if rows > 0:
            add = np.matrix([[0] * self.content.shape[1]] * rows)
            self.content = np.vstack([self.content, add])

    def fill(self):

        x, y = self.shape

        if x % 2 == 0:
            self.enlarge_to_shape(x + 1, y)
        if y % 2 == 0:
            self.enlarge_to_shape(x, y + 1)

    def set_value(self, row, column, value=1):
        self.content[row, column] = value

    def fold(self, index, axis):
        
        if axis == 'x':

            assert index * 2 == self.shape[1] - 1, "Not possible to fold"
            sub_matrix_a, sub_matrix_b = self.content[:, :index], self.content[:, (index+1):]

            assert sub_matrix_a.shape == sub_matrix_b.shape
            sub_matrix_b_flipped = np.fliplr(sub_matrix_b)

            self.content = np.maximum(sub_matrix_a, sub_matrix_b_flipped)
        
        elif axis == 'y':

            assert index * 2 == self.shape[0] - 1, "Not possible to fold"
            sub_matrix_a, sub_matrix_b = self.content[:index, :], self.content[(index+1):, :]

            assert sub_matrix_a.shape == sub_matrix_b.shape
            sub_matrix_b_flipped = np.flipud(sub_matrix_b)

            self.content = np.maximum(sub_matrix_a, sub_matrix_b_flipped)


if __name__ == "__main__":
    main()