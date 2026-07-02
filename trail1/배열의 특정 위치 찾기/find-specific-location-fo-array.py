arr = list(map(int, input().split()))

sum_1 = 0
sum_2 = 0
count = 0
for i in range(len(arr)):
    j = i+1
    if j % 2 == 0:
        sum_1 += arr[i]
    if j % 3 == 0:
        sum_2 += arr[i]
        count += 1
print(sum_1, round(sum_2/count, 1))
