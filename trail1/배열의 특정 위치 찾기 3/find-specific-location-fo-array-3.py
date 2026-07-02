arr = list(map(int, input().split()))

temp_arr = []
for i in arr:
    temp_arr.append(i)
    if i == 0:
        temp_arr.pop()
        break
sum_var = temp_arr[-3] + temp_arr[-2] + temp_arr[-1]
print(sum_var)