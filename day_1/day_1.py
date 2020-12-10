def get_data(filename):
    with open(filename, "r") as f:
        data = [int(line.strip()) for line in f]

    return data


data = get_data("input.txt")


def get_answer(data):
    for i in data:
        search_value = 2020 - i

        for j in data:
            if search_value == j:
                return search_value * i


print(get_answer(data))
