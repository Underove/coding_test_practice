a, b = map(int, input().split())

def is_even(n):
    sum = 0
    for i in range(0, len(str(n))):
        sum += int(str(n)[i])
    if sum % 2 == 0:
        return True
    else:
        return False

def is_prime(m):
    for j in range(2, m):
        if m % j == 0:
            return False
    return True

def solution(a, b):
    cnt = 0
    for i in range(a, b+1):
        if is_prime(i) and is_even(i):
            cnt += 1
        else:
            cnt += 0
    return cnt

print(solution(a, b))