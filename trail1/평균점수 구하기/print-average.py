arr = list(map(float, input().split()))

sum_var = 0
for i in arr:
    sum_var += i

print(round(sum_var/len(arr), 1))