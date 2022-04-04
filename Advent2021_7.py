import statistics as st

def load_data(file):

    with open(file) as op:

        input_list_strings = op.read()[:-1].split(',')[:]

    return input_list_strings

def count_total_distance_equal_cost(value, data: list):

    return sum([abs(d - value) for d in data])

def count_total_distance_appending_cost(value, data: list, by = 1):

    '''Used the sum of arithmetic sequence. Cost always starts at 1 and depends on the number of steps taken.'''
    return sum([((abs(d - value)*by + 1)/2)*(abs(d - value)) for d in data])

def main():

    data = load_data('Files/input7.txt')
    data = list(map(int, data))

    median = st.median(data)
    std = st.stdev(data)

    result1, result2 = [[float('inf'), float('inf')]] * 2

    for number in range(round(median - std/2), round(median + std/2)):

        if (suspect1 := count_total_distance_equal_cost(number, data)) < result1[0]:
            result1 = suspect1, number

        if (suspect2 := count_total_distance_appending_cost(number, data, by=1)) < result2[0]:
            result2 = suspect2, number

    print(f'Result1: {result1} \nResult2: {result2}')


if __name__ == "__main__":
    main()