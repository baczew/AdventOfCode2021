def load_data(file):

    with open(file) as op:

        input_list_strings = op.read().split(',')[:]

    return input_list_strings


class Fish:

    def __init__(self, age=8):

        self.child_list = []

        if 0 <= age <= 8:
            self.age = age
        else:
            raise ValueError('Fish cannot be that old')

    def __repr__(self):

        return f'F{self.age}{len(self.child_list)}{self.child_list}'

    def cycle(self):

        self.age -= 1

        for i in self.child_list:
            i.cycle()

        if self.age == -1:
            self.age = 6
            self.child_list.append(Fish(8))

        return f'I am {self.age} now', self.child_list


def count_kids(fish):

    count = 0

    for child in fish.child_list:
        count += count_kids(child)

    return count + 1

def count_pond(pond):

    count = 0

    for fish in pond:

        count += count_kids(fish)

    return count


def main():

    data = load_data('Files/input6.txt')

    pond = []

    for i in data:
        pond.append(Fish(int(i)))

    for c in range(80):
        for fish in pond:
            fish.cycle()

    number = count_pond(pond)
    print(number)

if __name__ == "__main__":
    main()



