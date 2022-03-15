from collections import Counter

def main():
    data = load_data('Files/input3.txt')
    #part1(data)
    part2(data)

def part2(input_data):
    y = calculate_rating(input_data, 'oxygen generator')
    x = calculate_rating(input_data, 'C02 scrubber')

    print(x*y)

def calculate_rating(input_data, rating):
    for i in range(len(input_data[0])):
        list_of_values = []

        for j in input_data:
            list_of_values.append(return_letter_no(j, i))

        if rating == 'oxygen generator':
            result = Counter(sorted(list_of_values, reverse=True)).most_common()[0][0]

        elif rating == 'C02 scrubber':
            result = Counter(sorted(list_of_values, reverse=True)).most_common()[-1][0]

        input_data = [x for x in input_data if int(x[i]) == result]

        if len(input_data) == 1:
            break

    return int(input_data[0], 2)

def part1(input_data):
    g = calculate_rate(input_data, 'gamma')
    print(g)
    e = calculate_rate(input_data, 'epsilon')
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