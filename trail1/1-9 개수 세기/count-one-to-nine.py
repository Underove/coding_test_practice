n = int(input())
arr = list(map(int, input().split()))

temp_arr = [0]*10

for elem in arr:
    temp_arr[elem] += 1

for i in temp_arr[1:]:
    print(i)
