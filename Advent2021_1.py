def main():
    data = load_data('Files/input1.txt')

    r_1 = count_increased(data)
    print(r_1)

    r_2 = count_increased_in_groups_of_three(data)
    print(r_2)

def load_data(file):

    with open(file) as op:
        input_list_strings = op.read().split('\n')[:-1]

    input_list_ints = list(map(int, input_list_strings))
    return input_list_ints

def count_increased(data):
    result = 0
    for index, mesurement in enumerate(data[1:]):
        if mesurement > data[index]:
            result += 1
    return result

def count_increased_in_groups_of_three(data):
    '''Insted of calculating sums we can just consider comparing two numbers that are not contained in both sums simultaneously'''
    result = 0
    for index, mesurement in enumerate(data[3:]):
        if mesurement > data[index]:
            result += 1
    return result

if __name__ == "__main__":
    main()