arr = [0]*11

arr[1], arr[2] = map(int, input().split())

for i in range(3, 11):
    arr[i] = arr[i-1] + arr[i-2]
    if arr[i] >= 10:
        arr[i] = arr[i] % 10

print(" ".join(map(str, arr[1:11])))