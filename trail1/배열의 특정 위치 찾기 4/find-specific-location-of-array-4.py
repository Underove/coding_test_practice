arr = list(map(int, input().split()))

count = 0
sum_var = 0
for i in arr:
    if i == 0:
        break
    if i % 2 == 0:
        count += 1
        sum_var += i
print(count, sum_var)