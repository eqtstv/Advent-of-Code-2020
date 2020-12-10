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
    print(i)
    letter = i[1]
    pos1 = int(i[0][0]) - 1
    pos2 = int(i[0][1]) - 1
    word = i[2]
    if word[pos1] != word[pos2] and (word[pos1] == letter) != (word[pos2] == letter):
        valid += 1

print(valid)