n, m = map(int, input().split())
grid = [
    list(map(int, input().split())) 
    for _ in range(n)
]

# 가능한 모든 모양
shapes = [
    [[1, 1, 0],
     [1, 0, 0],
     [0, 0, 0]],

    [[1, 1, 0],
     [0, 1, 0],
     [0, 0, 0]],

    [[0, 1, 0],
     [1, 1, 0],
     [0, 0, 0]],

    [[1, 0, 0],
     [1, 1, 0],
     [0, 0, 0]],
    
    [[1, 1, 1],
     [0, 0, 0],
     [0, 0, 0]],
    
    [[1, 0, 0],
     [1, 0, 0],
     [1, 0, 0]],
]

# 주어진 위치에 대해 가능한 모든 모양을 탐색하여 최대 합 반환
def get_sum(x, y):
    max_sum = 0
    for i in range(6): # 6가지 모양 1개씩
        is_possible = True
        sum = 0
        for dx in range(0, 3): # 3x3을 훑기
            for dy in range(0, 3):
                if shapes[i][dx][dy] == 0: # 없는 모양
                    continue
                if x + dx >= n or y + dy >= m: # 격자 밖이면
                    is_possible = False
                else:
                    sum += grid[x + dx][y + dy] # 덮은 칸 더하기
        if is_possible:
            max_sum = max(max_sum, sum)
    return max_sum

# 모든 위치에서 시도
ans = 0 # 지금까지 최고기록을 담는 변수
for i in range(n):
    for j in range(m):
        ans = max(ans, get_sum(i, j))

print(ans)