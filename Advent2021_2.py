
def main():

    data = load_data('input2.txt')
    right = sum_movement('forward', data)
    up = sum_movement('up', data)
    down = sum_movement('down', data)
    print((down - up) * right)

def sum_movement(mov, data):

    direction = [int(i.split()[1]) for i in data if i.split()[0] == mov]
    return sum(direction)

def load_data(file):

    with open(file) as op:
        input_list_strings = op.read().split('\n')[:-1]
    return input_list_strings

if __name__ == "__main__":
    main()
