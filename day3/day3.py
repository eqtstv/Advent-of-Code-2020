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


for j in range(5):
    for i in range(len(data)):
        data[i] += data[i]


cords = [0, 0]
count = 0
while cords[0] < len(data) or cords[1] < len(data):
    if check_position(cords, data):
        count += 1

    cords[0] += 1
    cords[1] += 3

print(count)