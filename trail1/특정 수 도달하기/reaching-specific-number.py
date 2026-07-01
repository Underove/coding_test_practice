arr = list(map(int, input().split()))

sum_val = 0
count = 0
for i in arr:
    if i >= 250:
        break
    sum_val += i
    count += 1

print(sum_val, round(sum_val/count, 1))