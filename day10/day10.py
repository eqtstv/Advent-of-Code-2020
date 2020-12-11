def get_data(filename):
    with open(filename, "r") as f:
        data = [int(line.strip()) for line in f]

    return data


data = sorted(get_data("input.txt"))

data.insert(0, 0)
data.append(data[-1] + 3)

count_1 = 0
count_3 = 0

for i in range(len(data) - 1):
    if data[i + 1] - data[i] == 1:
        count_1 += 1
    else:
        count_3 += 1

print(count_1 * count_3)
