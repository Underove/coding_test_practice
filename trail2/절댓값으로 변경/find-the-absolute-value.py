n = int(input())
arr = list(map(int, input().split()))

def solution(n, arr):
    for i in range(n):
        if arr[i] < 0:
            arr[i] = -arr[i]
    for j in arr:
        print(j, end= " ")

solution(n, arr)