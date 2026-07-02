arr = list(map(str, input().split()))

temp_arr = []
for i in range(1, len(arr), 3):
    temp_arr.append(arr[i])

print(" ".join(map(str, temp_arr)))