from collections import Counter

class Line():

    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2

    def __repr__(self):
        return 'First: ' + str(self.x1) + ' ' + str(self.y1) + '\n' + 'Second: ' + str(self.x2) + ' ' + str(self.y2)

    @property
    def straight(self):

        if self.x1 == self.x2:
            return True, 'Vertical'

        elif self.y1 == self.y2:
            return True, 'Horizontal'

        else:
            return False, 'Cross'

    def list_points(self):

        if 'Horizontal' in self.straight:
            y = self.y1
            x = min(self.x1, self.x2)
            while x <= max(self.x1, self.x2):
                yield x, y
                x+=1

        elif 'Vertical' in self.straight:
            y = min(self.y1, self.y2)
            x = self.x1
            while y <= max(self.y1, self.y2):
                yield x, y
                y+=1

        elif 'Cross' in self.straight:
            x = min(self.x1, self.x2)
            y = self.y1 if x == self.x1 else self.y2

            y_step = 1 if y == min(self.y1, self.y2) else -1

            while x <= max(self.x1, self.x2):
                yield x, y
                x+=1
                y+=y_step


def load_data(file):

    with open(file) as op:

        input_list_strings = op.read().split('\n')[:-1]

    return input_list_strings

def main():

    data = load_data('Files/input5.txt')

    list_of_points_straight = []
    list_of_points_cross = []

    for i in data:

        x = [list(map(int, z.split(','))) for z in i.split(' -> ')]

        if all(Line(*x[0], *x[1]).straight):

            for j in list(Line(*x[0], *x[1]).list_points()):
                list_of_points_straight.append(j)

        else:

            for j in list(Line(*x[0], *x[1]).list_points()):
                list_of_points_cross.append(j)


    #First part
    print(len([k for k in Counter(list_of_points_straight).most_common() if k[1] > 1]))

    #Second part
    print(len([k for k in Counter(list_of_points_straight+list_of_points_cross).most_common() if k[1] > 1]))



if __name__ == "__main__":
    main()