arr = list(map(int, input().split()))

temp_arr = []
for i in arr:
    temp_arr.append(i)
    if i == 0:
        temp_arr.pop()
        break
print(" ".join(map(str, temp_arr[::-1])))