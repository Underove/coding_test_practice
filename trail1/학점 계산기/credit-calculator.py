n = int(input())
arr = list(map(float, input().split()))

sum_val = 0 
for i in range(n):
    sum_val += arr[i]
aver_sum = sum_val / n
print(round(aver_sum, 1))

if aver_sum >= 4.0:
    print('Perfect')
elif aver_sum >= 3.0:
    print('Good')
else:
    print('Poor')