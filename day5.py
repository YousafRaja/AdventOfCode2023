from collections import defaultdict


TEST_FILE_NAME = 'test'
EXPECTED_TEST_ANSWER = 35
INPUT_FILE_NAME = 'input'


def parse_file(file_name):
    seeds = []
    maps = defaultdict(list)
    with open(file_name, 'r') as file:  
        index = -1          
        for line in file:
            if "seeds:" in line:
                seeds = [int(c) for c in line.split(":")[1].strip().split(" ")]
                continue 
            elif "map:" in line:
                index += 1
            elif len(line) > 1:
                maps[index].append([int(c) for c in line.strip().split()])
    return [seeds, maps]

def map_to_next(current, map):
    for row in map:
        d, s, r = row
        if s <= current <= (s+r):
            diff = current - s
            return d + diff 
    return current


def solution(file_name):
    seeds, maps = parse_file(file_name)
    lowest = float('inf')
    for seed in seeds:
        current = seed
        for key in maps:
            current = map_to_next(current, maps[key])
        lowest = min(lowest, current)
    return lowest

answer = solution(TEST_FILE_NAME)
print(answer)
assert answer == EXPECTED_TEST_ANSWER
answer = solution(INPUT_FILE_NAME)
print(answer)