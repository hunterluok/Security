

import numpy as np


class PringCircle:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def print_circle(self, data, startx, starty, rows, cols):
        row = startx
        col = starty
        while col < cols:
            print(data[row][col], end=" ")
            col += 1

        row += 1
        while row < rows:
            print(data[row][col - 1], end=" ")
            row += 1

        col -= 1
        while col > starty:
            print(data[row - 1][col - 1], end=" ")
            col -= 1

        col += 1
        row -= 1
        while row > startx + 1:
            print(data[row - 1][col - 1], end=" ")
            row -= 1
        return row, col

    def pirnt(self, data):
        rows, cols = data.shape
        startx = self.x
        starty = self.y
        while startx < rows and starty < cols:
            self.print_circle(data, startx, starty, rows, cols)
            startx += 1
            starty += 1
            rows -= 1
            cols -= 1


class PrintAno(PringCircle):
    def __init__(self, x, y):
        super(PrintAno, self).__init__()
        self.x = x
        self.y = y
        pass


    def print_circle(self, data, startx, starty, rows, cols):
        row = startx
        col = starty
        while col < cols:
            print(data[row][col], end=" ")
            col += 1

        row += 1
        while row < rows:
            print(data[row][col - 1], end=" ")
            row += 1

        col -= 1
        while col > 0:
            print(data[row - 1][col - 1], end=" ")
            col -= 1

        #col += 1
        row -= 1
        while row > 0 and (row-1 != startx or col-1 != starty):
            print(data[row - 1][col], end=" ")
            row -= 1
        return row, col

    def print(self, data):
        rows, cols = data.shape
        startx = self.x
        starty = self.y
        while startx < rows and starty < cols:
            self.print_circle(data, startx, starty, rows, cols)
            startx += 1
            starty += 1
            rows -= 1
            cols -= 1


if __name__ == "__main__":
    data = np.arange(9).reshape(3, 3)
    print("data is: \n {} \n".format(data))
    m, n = data.shape
    # my = PringCircle(x=0, y=1)
    #row, col = my.print_circle(data, 0, 0, m, n)
    # my.pirnt(data)

    my = PrintAno(x=0, y=2)
    print(my.print_circle(data, 0, 2, m, n))

