def get_data(filename):
    with open(filename, "r") as f:
        data = [line.strip() for line in f]

    return data


data = get_data("input.txt")


def check_position(cords, data):
    if data[cords[0]][cords[1]] == "#":
        return True
    else:
        return False


def check_slope(data, x, y):
    cords = [0, 0]
    count = 0
    while cords[0] < len(data):
        if check_position(cords, data):
            count += 1

        cords[0] += y
        cords[1] += x
    return count


for j in range(10):
    for i in range(len(data)):
        data[i] += data[i]

one_one = check_slope(data, 1, 1)
three_one = check_slope(data, 3, 1)
five_one = check_slope(data, 5, 1)
seven_one = check_slope(data, 7, 1)
one_two = check_slope(data, 1, 2)


print(one_one * three_one * five_one * seven_one * one_two)
