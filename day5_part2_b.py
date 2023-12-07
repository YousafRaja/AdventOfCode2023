from collections import defaultdict

# For each seed
# 1. Calculate the maximum range
# 2. Map this range by before, mapped and after
#   - before is the sub-range which exists before the next mappable range
#   - mapped is the sub-range which overlaps exactly with the next mappable range
#   - after is the sub-range which extends past the next mappable range 
# Take the non-null sub-ranges from step 2 and repeat the process for the next mapping
# 3. After going through all the maps, the last map will be a list of sub-ranges representing locations. We only care about the first value in the lowest range.



TEST_FILE_NAME = 'test'
EXPECTED_TEST_ANSWER = 46
INPUT_FILE_NAME = 'input'
MAPS = defaultdict(list)

def parse_file(file_name):
    seeds = []
    with open(file_name, 'r') as file:  
        index = -1          
        for line in file:
            if "seeds:" in line:
                seeds = [int(c) for c in line.split(":")[1].strip().split(" ")]
                continue 
            elif "map:" in line:
                index += 1
            elif len(line) > 1:
                MAPS[index].append([int(c) for c in line.strip().split()])
    return seeds

def map_to_row(source: int, row) -> int | None:
    diff = source - row[1]
    if diff >= 0 and diff < row[2]:
        return row[0] + diff
    return None


def map_multi_range(source, current_row):
    before, mapped, after = None, None, None
    start, end = current_row[1], current_row[1] + current_row[2] - 1
    if start > source[0]:
        before = (source[0], min(source[1], start - 1))
    if start <= source[1] and end >= source[0]:
        maxStart = max(source[0], start)
        minEnd = min(source[1], end)
        mapped = (map_to_row(maxStart, current_row), map_to_row(minEnd, current_row))
    if end < source[1]:
        after = (max(source[0], end + 1), source[1])
    return (before, mapped, after)

def map_current_range(source: tuple[int, int], key):
   result = []
   toMap = [source]
   for m in MAPS[key]:
        next = []
        for tm in toMap:
            before, mapped, after = map_multi_range(tm, m)
            if before:
                next.append(before)
            if mapped:
                result.append(mapped)
            if after:
                next.append(after)
        toMap = next
   result.extend(toMap)
   return result 
           

def solution(file_name):
    seeds = parse_file(file_name)    
    MAPS[len(MAPS)-1].sort()
    seed_list = []
    for i in range(0, len(seeds), 2):
        seed_list.append([seeds[i], seeds[i] + seeds[i+1] - 1])

    locations = []
    for pair in seed_list:
        sr_list = [pair]
        for key in MAPS:
            next = []
            for sr in sr_list:
                next += map_current_range(sr, key)
            sr_list = next  
            next = []
        locations.append(min(sr_list)[0])
            
    return min(locations)

answer = solution(TEST_FILE_NAME)
print(answer)
assert answer == EXPECTED_TEST_ANSWER
MAPS = defaultdict(list)
answer = solution(INPUT_FILE_NAME)
print(answer)