import numpy as np
import heapq

def load_data(file):

    with open(file) as op:

        input_list_of_lists = [list(map(int, line[:-1])) for line in op.readlines()]

        input_numpy_array = np.array(input_list_of_lists)

    return input_numpy_array



def get_adjacent_values(matrix, initial_row, initial_column):

    directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]

    values = []
    positions = []

    for direction in directions:

        current_row = initial_row + direction[0]
        current_col = initial_column + direction[1]

        try:
            if (current_row < 0) or (current_col < 0):
                raise IndexError('Out!')
            values.append(matrix[current_row, current_col])
            positions.append(tuple([current_row, current_col]))
        except IndexError:
            continue

    return values, positions



def control_arg(func):

    prev_call = []

    def inner_function(*args, **kwargs):

        if args[1:] in prev_call:
            return 0

        else:
            prev_call.append(args[1:])
            result = func(*args, **kwargs)

        return result

    return inner_function



@control_arg
def filter_bigger_adjacent_values_and_count(matrix, initial_row, initial_column):

    value, position = get_adjacent_values(matrix, initial_row, initial_column)

    v_and_p = zip(value, position)

    filtered = [i for i in v_and_p if (9 > i[0] > matrix[initial_row, initial_column])]

    return 1 + sum([filter_bigger_adjacent_values_and_count(matrix, *point[1]) for point in filtered])



def get_prod_of_n_from_the_heap(n:int, heap:heapq):

    return abs(np.prod([heapq.heappop(heap) for _ in range(n)]))



def task1():

    data = load_data('Files/input9.txt')

    low_points_matrix = np.empty(shape=data.shape)

    for column in range(data.shape[1]):
        for row in range(data.shape[0]):
            low_points_matrix[row, column] = data[row, column] + 1 \
                                             if data[row, column] < min(get_adjacent_values(data, row, column)[0]) \
                                             else np.nan

    return data, low_points_matrix



def task2():

    data, low_points_matrix = task1()

    group = []
    heapq.heapify(group)

    for column in range(low_points_matrix.shape[1]):
        for row in range(low_points_matrix.shape[0]):
            if np.isnan(low_points_matrix[row, column]):
                continue
            else:
                heapq.heappush(group, filter_bigger_adjacent_values_and_count(data, row, column) * (-1))

    return get_prod_of_n_from_the_heap(3, group)



def main():
    result1 = task1()
    print(f'Result of task 1: {np.nansum(result1):.0f}')

    result2 = task2()
    print(f'Result of task 2: {result2:.0f}')



if __name__ == "__main__":
    main()