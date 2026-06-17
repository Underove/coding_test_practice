n, m = map(int, input().split())

def number(n, m):
    num = 0
    for i in range(1, min(n, m)+1):
        if n % i == 0 and m % i == 0:
            num = i
    print(num)

number(n, m)
