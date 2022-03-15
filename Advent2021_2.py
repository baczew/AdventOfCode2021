
def main():

    data = load_data('Files/input2.txt')
    part1(data)
    part2(data)

def sum_movement(mov, data):

    direction = [int(i.split()[1]) for i in data if i.split()[0] == mov]
    return sum(direction)

def load_data(file):

    with open(file) as op:
        input_list_strings = op.read().split('\n')[:-1]
    return input_list_strings

def tic_tac(func):

    import time
    def inner(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        exec_time = end_time - start_time
        print(f'Execution took: {exec_time}')
        return result
    return inner

@tic_tac
def part1(data1):

    right = sum_movement('forward', data1)
    up = sum_movement('up', data1)
    down = sum_movement('down', data1)

    print((down - up) * right)

@tic_tac
def part2(data2):

    aim = 0
    right = 0
    depth = 0

    for i in data2:

        if i.split()[0] == 'down':
            aim += int(i.split()[1])

        elif i.split()[0] == 'up':
            aim -= int(i.split()[1])

        elif i.split()[0] == 'forward':
            depth += int(i.split()[1]) * aim
            right += int(i.split()[1])

    print(right * depth)

if __name__ == "__main__":
    main()
