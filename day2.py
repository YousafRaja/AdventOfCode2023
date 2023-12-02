

from collections import defaultdict


input_file = 'input'

def get_new_bag():
    return defaultdict(list, (('red', 12), ('green', 13), ('blue', 14)))

def get_empty_bag():
    return defaultdict(list, (('red', 0), ('green', 0), ('blue', 0)))

# Part One
def valid_count(line):
    grabs = line[line.find(":")+1:].split(";")
    for grab in grabs:
        bag = get_new_bag()
        colors = grab.split(",")
        for color in colors:
            count_and_type = color.split()
            bag[count_and_type[1]] -= int(count_and_type[0])
            if bag[count_and_type[1]] < 0:
                return 0
    return int(line.split(":")[0].split()[1])

# Part Two
def get_powerset(line):
    grabs = line[line.find(":")+1:].split(";")
    bag = get_empty_bag()
    for grab in grabs:
        colors = grab.split(",")
        for color in colors:
            count_and_type = color.split()
            bag[count_and_type[1]] = max(bag[count_and_type[1]], int(count_and_type[0]))

    return bag["red"]*bag["green"]*bag["blue"]


with open(input_file, 'r') as file:
    
    valid_total = 0
    for line in file:
        valid_total += get_powerset(line)
    print(valid_total)

