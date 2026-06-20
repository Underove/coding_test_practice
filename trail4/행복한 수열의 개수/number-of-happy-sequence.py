n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

seq = [0 for _ in range(n)]

def is_happy():
    consecutive_count = 1 # 현재 연속 길이
    max_count = 1 # 최고 연속 길이
    for i in range(1, n):
        if seq[i-1] == seq[i]:
            consecutive_count += 1
        else:
            consecutive_count = 1
        
        max_count = max(consecutive_count, max_count)

    return max_count >= m # 최대 연속 회수가 m이상이면 True

num_happy = 0
# 가로줄 검사
for i in range(n):
    seq = grid[i][:] # [:] = 전체 복사 의미
    if is_happy():
        num_happy += 1

# 세로줄 검사
for j in range(n):
    for i in range(n):
        seq[i] = grid[i][j] 
    if is_happy():
        num_happy += 1

print(num_happy)