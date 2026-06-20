n = int(input())
grid = [
    list(map(int, input().split())) 
    for _ in range(n)
]

# (row_s, col_s) -> 1x1 지점
# (row_e, col_e) -> 3x3 지점

def get_gold(row_s, col_s, row_e, col_e):
    num_gold = 0

    for row in range(row_s, row_e+1):
        for col in range(col_s, col_e+1):
            num_gold += grid[row][col]
    return num_gold

max_gold = 0
for row in range(n):
    for col in range(n):
        if row + 2 >= n or col + 2 >= n: # 벗어나는 경우
            continue
        
        num_gold = get_gold(row, col, row + 2, col + 2)

        max_gold = max(max_gold, num_gold)

print(max_gold)

