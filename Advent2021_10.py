from collections import deque

def load_data(file):

    with open(file) as op:

        input_list_of_lists = [line[:-1] for line in op.readlines()]

    return input_list_of_lists

def line_analyze(line, openings, closings):

    stack = deque()
    pairs = dict(zip(openings, closings))

    for sign in line:
        if sign in openings:
            stack.append(sign)
        elif pairs[stack.pop()] == sign:
            continue
        else:
            return sign


def main():

    data = load_data('Files/input10.txt')

    cost_dict = {')': 3, ']': 57, '}': 1197, '>': 25137}
    bracket_open = ('(', '{', '[', '<')
    bracket_close = (')', '}', ']', '>')

    cost_list = []

    for line in data:

        corrupted = line_analyze(line, bracket_open, bracket_close)
        cost_list.append(cost_dict[corrupted]) if cost_dict.get(corrupted, False) else 0

    print(sum(cost_list))

if __name__ == "__main__":
    main()