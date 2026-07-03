arr = list(map(int, input().split()))

temp_arr = []
for i in arr:
    if i == 0:
        break
    if i % 2 == 0:
        temp_arr.append(i//2)
    else:
        temp_arr.append(i+3)
print(" ".join(map(str, temp_arr)))