

class MaxGigt:
    def __init__(self):
        pass

    def cal_gift(self, data, row=0, col=0):
        rows = len(data)
        cols = len(data[0])
        sums = data[row][col]

        print("rows is {}, cols is {}".format(rows, cols))

        while row < rows:
            while col < cols:
                # if col == 0 and row == 0:
                #     sums += data[col][row]
                #     continue
                # 这种搞法是有问题的。陷入死循环中去了。
                #到达边界之后就只有一条路可以走了。
                if col == cols-1 and row < rows-1:
                    # 这里注意对列别的处理方式不同，需要特别注意。
                    print("row is {}, col is {}".format(row, col))
                    for index in range(row+1, rows):
                        sums += data[index][col]
                    return sums
                if row == rows-1 and col < cols-1:
                    sums += sum(data[row][col+1: cols])
                    return sums

                temp_col = data[row][col+1]
                temp_row = data[row+1][col]
                if temp_col > temp_row:
                    print(temp_col, "temp_col")
                    col += 1
                    sums += temp_col
                else:
                    print(temp_row, "temp_row")
                    row += 1
                    sums += temp_row


if __name__ == "__main__":
    data = [[1, 13, 3, 8],
            [12, 2, 9, 6],
            [5, 7, 4, 11],
            [3, 7, 16, 5]]
    my = MaxGigt()
    result = my.cal_gift(data)
    print(result)
    print(sum(data[0][2:4]))

