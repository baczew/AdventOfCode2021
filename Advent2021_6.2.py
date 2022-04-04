from collections import Counter

def load_data(file):

    with open(file) as op:

        input_list_strings = op.read()[:-1].split(',')[:]

    return input_list_strings

def cycle(pond: dict, n: int):

    for cycle in range(n):

        pond['0'], pond['1'], pond['2'], pond['3'], pond['4'], pond['5'], pond['6'], pond['7'], pond['8'] = \
        pond['1'], pond['2'], pond['3'], pond['4'], pond['5'], pond['6'], pond['7'], pond['8'], pond['0']
        pond['6'] += pond['8']

    return pond

def main():

    data = load_data('Files/input6.txt')

    data_counted = dict(Counter(data))
    data_counted_sorted = dict()

    for i in range(9):
        data_counted_sorted[str(i)] = data_counted.get(str(i), 0)

    results = cycle(data_counted_sorted, 256)
    print(sum([x for x in results.values()]))

if __name__ == "__main__":
    main()



