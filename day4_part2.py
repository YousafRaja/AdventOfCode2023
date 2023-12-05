from collections import defaultdict


TEST_FILE_NAME = 'test'
EXPECTED_TEST_ANSWER = 30
INPUT_FILE_NAME = 'input'

def get_wins(line):
    line = line.strip()
    processed_line = line.split(":")[1].split("|")
    winning_numbers = set(processed_line[0].split())
    actual_numbers = set(processed_line[1].split())
    wins = 0
    for number in actual_numbers:
        wins += number in winning_numbers
    return wins 


def get_graph(file_name):
    adj_list = defaultdict(list)
    current_card_number = 0
    with open(file_name, 'r') as file:
        for line in file:
             current_card_number += 1
             adj_list[current_card_number] = []
             next_card_count = get_wins(line)
             while next_card_count:
                 adj_list[current_card_number].append(current_card_number + next_card_count)
                 next_card_count -= 1

    return adj_list

def dfs(card_number, adj_list):
    count = 0
    for nei in adj_list[card_number]:
        count += dfs(nei, adj_list)
    return 1 + count 



def solution(file_name):
    adj_list = get_graph(file_name)
    total_card_count = 0
    for i in range(1, len(adj_list)+1):
        total_card_count += dfs(i, adj_list)
    return total_card_count

answer = solution(TEST_FILE_NAME)
print(answer)
assert answer == EXPECTED_TEST_ANSWER
answer = solution(INPUT_FILE_NAME)
print(answer)