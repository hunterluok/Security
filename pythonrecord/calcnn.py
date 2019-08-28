

import numpy as np
d1 = np.array([[1, 2, 3, 4], [3, 2, 1, 2], [2, 2, 1, 3]])
kenel = np.array([[1, -1], [-1, 1]])


def con(d1, kenel, strde=2):
    m, n = kenel.shape
    md, nd= d1.shape
    row_index = int((md - m) / strde) + 1
    col_index = int(( nd - n) / strde) + 1
    print(row_index, col_index)
    result = []
    for row  in range(row_index):
        temp_row = []
        for col in range(col_index):
            temp_data = d1[row : row + m,  col : col + n]
            res = np.sum(np.multiply(temp_data, kenel))
            temp_row.append(res)
        result.append(temp_row)
    return result


if __name__ == "__main__":
    print(con(d1, kenel))