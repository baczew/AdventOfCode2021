def load_data(file):

    with open(file) as op:

        input_list_strings = op.read().split(',')[:]

    return input_list_strings


class Fish:

    number_of_instances = 0

    def __init__(self, age=8):

        Fish.number_of_instances += 1

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


def main():

    data = load_data('Files/input6.txt')

    pond = []

    for i in data:
        pond.append(Fish(int(i)))

    for c in range(80):
        for fish in pond:
            fish.cycle()

    print(Fish.number_of_instances)

if __name__ == "__main__":
    main()



