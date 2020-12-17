def get_data(filename):
    with open(filename, "r") as f:
        data = [int(line.strip()) for line in f]

    return data


data = get_data("input.txt")


def get_answer(data):
    for i in data:
        for j in data:
            for k in data:
                if i + j + k == 2020:
                    return i * j * k


print(get_answer(data))