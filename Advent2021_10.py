from collections import deque

def main():

    data = load_data('Files/input10.txt')
    part1(data)
    part2(data)

def part1(data_arg):

    cost_dict = {')': 3, ']': 57, '}': 1197, '>': 25137}
    bracket_open = ('(', '{', '[', '<')
    bracket_close = (')', '}', ']', '>')

    cost_list = []

    for line in data_arg:
        is_corr = is_corrupted(line, bracket_open, bracket_close)
        if isinstance(is_corr, str):
            corrupted = is_corr
            cost_list.append(cost_dict[corrupted]) if cost_dict.get(corrupted, False) else 0

    print(sum(cost_list))


def part2(data_arg):

    cost_dict = {')': 1, ']': 2, '}': 3, '>': 4}
    bracket_open = ('(', '{', '[', '<')
    bracket_close = (')', '}', ']', '>')

    cost_list = []

    for line in data_arg:

        is_corr = is_corrupted(line, bracket_open, bracket_close)

        if isinstance(is_corr, list):
            line_score = 0
            for bracket in is_corr:
                line_score *= 5
                line_score += cost_dict.get(bracket)
            cost_list.append(line_score)

    print(sorted(cost_list)[int(len(cost_list)/2 - 0.5)])

def load_data(file):

    with open(file) as op:

        input_list_of_lists = [line[:-1] for line in op.readlines()]

    return input_list_of_lists

def is_corrupted(line, openings, closings):

    stack = deque()
    pairs = dict(zip(openings, closings))

    for sign in line:

        if sign in openings:
            stack.append(sign)

        elif pairs[stack.pop()] == sign:
            continue

        else:
            return sign

    return [pairs.get(i) for i in reversed(stack)]


if __name__ == "__main__":
    main()