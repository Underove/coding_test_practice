arr = list(map(int, input().split()))
temp_arr = [0]*11

for elem in arr:
    if elem == 0:
        break
    num = (elem // 10)
    temp_arr[num] += 1

i = 100
arr_2 = temp_arr[::-1]
for j in arr_2[:-1]:
    print(f'{i} - {j}')
    i -= 10