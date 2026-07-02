arr = list(map(int, input().split()))

temp_arr = []
for i in arr:
    temp_arr.append(i)
    if i == 0:
        temp_arr.pop()
        break
amount = sum(temp_arr)
aver_var = round(amount / len(temp_arr), 1)

print(amount, aver_var)