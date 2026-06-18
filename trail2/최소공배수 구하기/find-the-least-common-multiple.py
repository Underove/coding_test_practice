n, m = map(int, input().split())

def number(n, m):
    num = max(n, m)
    while True:
        if num % n == 0 and num % m == 0:
            return num
        num += 1

print(number(n,m))
        