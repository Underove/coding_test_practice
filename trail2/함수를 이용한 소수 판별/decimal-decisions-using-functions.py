a, b = map(int, input().split())

def is_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def solution(a, b):
    sum = 0
    for j in range(a, b+1):
        if is_prime(j):
            sum += j
    return sum

print(solution(a, b))