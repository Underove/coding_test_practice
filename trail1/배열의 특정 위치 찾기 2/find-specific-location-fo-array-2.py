arr = list(map(int, input().split()))

sum_odd = 0
sum_even = 0
for i in range(len(arr)):
    j = i+1
    if i % 2 == 0:
        sum_even += arr[i]
    else:
        sum_odd += arr[i]
print(abs(sum_odd - sum_even))