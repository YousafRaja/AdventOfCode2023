TEST_FILE_NAME = 'test'
EXPECTED_TEST_ANSWER = 13
INPUT_FILE_NAME = 'input'

def get_wins(line):
    line = line.strip()
    processed_line = line.split(":")[1].split("|")
    winning_numbers = set(processed_line[0].split())
    actual_numbers = set(processed_line[1].split())
    wins = 0
    for number in actual_numbers:
        if number in winning_numbers:
            wins = 1 if wins == 0 else wins*2
    return wins 


def solution(file_name):
    total_wins = 0
    with open(file_name, 'r') as file:            
        for line in file:
            total_wins += get_wins(line)
    return total_wins

answer = solution(TEST_FILE_NAME)
print(answer)
assert answer == EXPECTED_TEST_ANSWER
answer = solution(INPUT_FILE_NAME)
print(answer)