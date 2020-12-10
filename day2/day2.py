def get_data(filename):
    with open(filename, "r") as f:
        data = [line.strip() for line in f]

    return data


data = get_data("input.txt")


parsed_data = [
    [line.split()[0].split("-"), line.split()[1][0], line.split()[2]] for line in data
]

valid = 0
for i in parsed_data:
    letter = i[1]
    count = i[2].count(letter)
    if int(i[0][0]) <= count <= int(i[0][1]):
        valid += 1

print(valid)