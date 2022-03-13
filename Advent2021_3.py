def main():
    data = load_data('Files/input3.txt')
    g = calculate_rate(data, 'gamma')
    print(g)
    e = calculate_rate(data, 'epsilon')
    print(e)
    print(int(g, 2) * int(e, 2))

def calculate_rate(input_data, rate):
    result = []
    for i in range(len(input_data[0])):
        list_of_values = []
        for j in input_data:
            list_of_values.append(return_letter_no(j, i))
        if rate == 'gamma':
            result.append(max(set(list_of_values), key=list_of_values.count))
        elif rate == 'epsilon':
            result.append(min(set(list_of_values), key=list_of_values.count))
    return ''.join(str(element) for element in result)

def return_letter_no(string, number):
    return int(string[number])

def load_data(file):
    with open(file) as op:
        input_list_strings = op.read().split('\n')[:-1]
    return input_list_strings

if __name__ == "__main__":
    main()