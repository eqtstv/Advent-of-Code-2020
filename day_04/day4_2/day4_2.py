def get_data(filename):
    with open("input.txt") as f:
        lines = f.read()

    return lines.split("\n\n")


data = get_data("input.txt")
data = [line.replace("\n", " ").split(" ") for line in data]

req = {
    "byr": [1920, 2002],
    "iyr": [2010, 2020],
    "eyr": [2020, 2030],
    "hgt": [150, 193, 59, 76],
    "hcl": [
        "0",
        "1",
        "2",
        "3",
        "4",
        "5",
        "6",
        "7",
        "8",
        "9",
        "a",
        "b",
        "c",
        "d",
        "e",
        "f",
    ],
    "ecl": ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"],
    "pid": [9],
}


def check_value(value, req):
    if value[0] in ["byr", "iyr", "eyr"]:
        if req[value[0]][0] <= int(value[1]) <= req[value[0]][1]:
            return True
        else:
            return False

    if value[0] == "hgt":
        if value[1][-2:] == "cm":
            if req[value[0]][0] <= int(value[1][:-2]) <= req[value[0]][1]:
                return True
            else:
                return False
        elif value[1][-2:] == "in":
            if req[value[0]][2] <= int(value[1][:-2]) <= req[value[0]][3]:
                return True
            else:
                return False

    if value[0] == "hcl":
        if value[1][0] == "#":
            if sum([char in req[value[0]] for char in value[1][1:]]) == 6:
                return True
            else:
                return False

    if value[0] == "ecl":
        if value[1] in req[value[0]]:
            return True
        else:
            return False

    if value[0] == "pid":
        if len(value[1]) == 9:
            return True
        else:
            return False

    if value[0] == "cid":
        return False

    else:
        return False


count = 0
for entry in data:
    entry = [val.split(":") for val in entry]
    if sum([val[0] in req.keys() for val in entry]) == 7:
        control_sum = 0
        for val in entry:
            control_sum += check_value(val, req)
        if control_sum == 7:
            count += 1

print(count)