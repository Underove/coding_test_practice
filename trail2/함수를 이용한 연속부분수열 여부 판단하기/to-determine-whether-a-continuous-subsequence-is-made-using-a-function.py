n1, n2 = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

def solution(n1, n2):
    for i in range(n1 - n2 + 1):
        if a[i:i+n2] == b:
            return 'Yes'
    return 'No'

print(solution(n1, n2))