n = int(input())
arr = list(map(int, input().split()))

temp_arr = []
for i in arr:
    if i % 2 == 0:
        temp_arr.append(i)
print(" ".join(map(str, temp_arr[::-1])))