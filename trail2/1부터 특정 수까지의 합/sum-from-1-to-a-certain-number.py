n = int(input())

def solution(n):
    sum = 0
    for i in range(1, n+1):
        sum += i
    return int(sum / 10)

print(solution(n))