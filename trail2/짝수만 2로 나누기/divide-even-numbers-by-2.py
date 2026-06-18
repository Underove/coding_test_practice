n = int(input())
arr = list(map(int, input().split()))

def solution(n, arr):
    for i in range(n):
        if arr[i] % 2 == 0:
            arr[i] = arr[i] // 2
    for elem in arr:
        print(elem, end= " ")

solution(n, arr)