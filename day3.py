test_file_name = 'test'
input_file_name = 'input'

PART_NUMBERS = []

def remove_full_number(i, j, grid):
    left = j
    right = j  
    while (left-1)>=0 and grid[i][left-1].isnumeric():
        left -= 1
    while (right+1)<len(grid[i]) and grid[i][right+1].isnumeric():
        right += 1    
    full_number = grid[i][left:right+1]
    PART_NUMBERS.append(int(full_number))
    grid[i] = grid[i][:left] + "".join(["." for _ in full_number]) + grid[i][right+1:]

def check_surrondings(row, col, grid):
    offsets = [[-1, -1], [-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1], [0, -1]]
    for delta in offsets:
        dy, dx = delta
        y, x = dy + row, dx + col 
        if y >= 0 and y < len(grid) and x >= 0 and x < len(grid[row]):
            if grid[y][x].isnumeric():
                remove_full_number(y, x, grid) 

def solution(file_name):
    with open(file_name, 'r') as file:            
        grid = []
        for line in file:
            line = line.strip()
            grid.append(line)    
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if not grid[row][col].isnumeric() and grid[row][col] != ".":
                check_surrondings(row, col, grid)
    return sum(PART_NUMBERS)

        
answer = solution(test_file_name)
print(answer)
assert answer == 4361
PART_NUMBERS = []
answer = solution(input_file_name)
print(answer)
