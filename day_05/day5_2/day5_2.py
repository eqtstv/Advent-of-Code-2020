def get_data(filename):
    with open(filename, "r") as f:
        data = [line.strip() for line in f]

    return data


data = get_data("input.txt")


def select_seat(cords, letter, let):
    cords[int(letter == let)] = cords[1] - (cords[1] - cords[0]) // 2
    return cords


def find_missing(lst):
    return [x for x in range(lst[0], lst[-1] + 1) if x not in lst]


seats = []
for entry in data:
    no_rows = [0, 127]
    no_columns = [0, 7]
    for letter in entry[:-3]:
        select_seat(no_rows, letter, "F")

    for letter in entry[-3:]:
        select_seat(no_columns, letter, "L")

    seats.append(no_rows[0] * 8 + no_columns[0])

print(find_missing(sorted(seats))[0])