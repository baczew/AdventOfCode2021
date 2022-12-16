from collections import Counter

def main():

    data = load_data('C:/Users/mateusz.baczewski/PythonProjects/AdventOfCode2021/Files/input08.txt')
    #part1(data)
    part2(data)


def load_data(file):

    with open(file) as op:
        input_list_of_lists = [line[:-1] for line in op.readlines()]

    return input_list_of_lists


def part1(data):

    code = {
        "0": {"a", "b", "c", "e", "f", "g"},
        "1": {"c", "f"},
        "2": {"a", "c", "d", "e", "g"},
        "3": {"a", "c", "d", "f", "g"},
        "4": {"b", "c", "d", "f"},
        "5": {"a", "b", "d", "f", "g"},
        "6": {"a", "b", "d", "e", "f", "g"},
        "7": {"a", "c", "f"},
        "8": {"a", "b", "c", "d", "e", "f", "g"},
        "9": {"a", "b", "c", "d", "f", "g"}
    }

    code_len = {k: len(v) for k, v in code.items()}
    lens_occurances = dict(Counter([v for k, v in code_len.items()]))
    unique_lens = [k for k, v in lens_occurances.items() if v == 1]
    numbers_with_unique_lens = [k for k, v in code_len.items() if v in unique_lens]
    count = {k: 0 for k in numbers_with_unique_lens}

    for line in data:
        output_part = line.split("|")[-1].strip()

        for output_digit in output_part.split(" "):

            if len(output_digit) in list(unique_lens):

                number_represented = max([k for k, v in code_len.items() if v == len(output_digit)])
                count[number_represented] += 1


    print(f"Final counting dictionary: {count}")
    print(f"Sum: {sum([v for k, v in count.items()])}")


def part2(data):

    code = {
        "0": {"a", "b", "c", "e", "f", "g"},
        "1": {"c", "f"},
        "2": {"a", "c", "d", "e", "g"},
        "3": {"a", "c", "d", "f", "g"},
        "4": {"b", "c", "d", "f"},
        "5": {"a", "b", "d", "f", "g"},
        "6": {"a", "b", "d", "e", "f", "g"},
        "7": {"a", "c", "f"},
        "8": {"a", "b", "c", "d", "e", "f", "g"},
        "9": {"a", "b", "c", "d", "f", "g"}
    }

    code_len = {k: len(v) for k, v in code.items()}

    results = []

    for line in data:

        input_part = line.split("|")[0].strip()
        output_part = line.split("|")[-1].strip()

        set_input_parts = [set(x) for x in input_part.split(" ")]
        set_output_parts = [set(x) for x in output_part.split(" ")]
        identification_list = [None] * 10

        # Identify 1, 7, 4, 8
        identification_list[1] = set(max([i for i in set_input_parts if len(i) == code_len['1']]))
        identification_list[7] = set(max([i for i in set_input_parts if len(i) == code_len['7']]))
        identification_list[4] = set(max([i for i in set_input_parts if len(i) == code_len['4']]))
        identification_list[8] = set(max([i for i in set_input_parts if len(i) == code_len['8']]))
        set_input_parts = [i for i in set_input_parts if i not in identification_list]

        # Identify 0
        for element in set_input_parts:
            if len(element & identification_list[4]) == 3 and len(element & identification_list[7]) == 3 and len(element) == 6:
                identification_list[0] = element
        set_input_parts = [i for i in set_input_parts if i not in identification_list]

        # Identify 9
        for element in set_input_parts:
            if len(element & identification_list[4]) == 4 and len(element & identification_list[7]) == 3 and len(element) == 6:
                x+=1
                identification_list[9] = element
        assert x == 1, "Identified 9 onced"
        set_input_parts = [i for i in set_input_parts if i not in identification_list]

         # Identify 6
        for element in set_input_parts:
            if len(element & identification_list[4]) == 3 and len(element & identification_list[7]) == 2 and len(element) == 6:
                identification_list[6] = element
        set_input_parts = [i for i in set_input_parts if i not in identification_list]

        # Identify 3
        for element in set_input_parts:
            if len(element & identification_list[1]) == 2 and len(element) == 5:
                identification_list[3] = element
        set_input_parts = [i for i in set_input_parts if i not in identification_list]

        # Identify 2
        for element in set_input_parts:
            if len(element & identification_list[9]) == 4 and len(element) == 5:
                identification_list[2] = element
        set_input_parts = [i for i in set_input_parts if i not in identification_list]

        # Identify 5
        identification_list[5], *_ = set_input_parts

        result_list = [str(identification_list.index(number)) for number in set_output_parts]
        results.append(int(''.join(result_list)))
    
    print(sum(results))


if __name__ == "__main__":
    main()