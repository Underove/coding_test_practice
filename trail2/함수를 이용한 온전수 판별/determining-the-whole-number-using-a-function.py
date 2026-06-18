a, b = map(int, input().split())

def solution(a, b):
    cnt = 0
    for i in range(a, b+1):
        if i % 2 == 0 or str(i)[-1] == '5' or (i % 3 == 0 and i % 9 != 0):
            cnt += 0
        else:
            cnt += 1
    return cnt

print(solution(a, b))