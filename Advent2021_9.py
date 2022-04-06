import numpy as np

def load_data(file):

    with open(file) as op:

        input_list_of_lists = [list(map(int, line[:-1])) for line in op.readlines()]

        input_numpy_array = np.array(input_list_of_lists)

    return input_numpy_array

def get_adjacent_values(matrix, initial_row, initial_column):

    directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]

    values = []

    for direction in directions:

        try:
            if (initial_row + direction[0] < 0) or (initial_column + direction[1] < 0):
                raise IndexError('Out!')
            values.append(matrix[initial_row + direction[0], initial_column + direction[1]])
        except IndexError:
            continue

    return values


def main():

    data = load_data('Files/input9.txt')

    low_points_matrix = np.empty(shape=data.shape)

    for column in range(data.shape[1]):
        for row in range(data.shape[0]):
            low_points_matrix[row, column] = data[row, column] + 1 if data[row, column] < min(get_adjacent_values(data, row, column)) else np.nan

    print(f'{np.nansum(low_points_matrix):.0f}')


if __name__ == "__main__":
    main()