def get_data(filename):
    with open("input.txt") as f:
        lines = f.read()

    return lines.split("\n\n")


data = get_data("input.txt")


required_fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]

count = 0
for entry in data:
    if sum([val in entry for val in required_fields]) == 7:
        count += 1

print(count)