arr = list(map(int, input().split()))

temp_arr = [0]*7
for elem in arr:
    temp_arr[elem] += 1

i = 1
for j in temp_arr[1:]:
    print(f'{i} - {j}')
    i += 1