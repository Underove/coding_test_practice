arr = list(map(int, input().split()))

temp_arr = [0]*10

for elem in arr:
    if elem == 0:
        break
    num = (elem // 10) % 10
    temp_arr[num] += 1

i = 1
for j in temp_arr[1:]:
    print(f'{i} - {j}')
    i += 1
