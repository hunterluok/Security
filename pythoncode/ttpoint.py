


def get_data(data):

    mylist = []
    temp_x = 0
    temp_y = 0
    for line in data:
        x, y = line[0], line[1]
        if y > temp_y:
            temp_y = y
        if x > temp_x:
            temp_x = x