a, b = map(int, input().split())

def solution(a, b):
    if a > b:
        a *= 2
        b += 10
    else:
        a += 10
        b *= 2
    return a, b

a, b = solution(a, b)
print(a, b)