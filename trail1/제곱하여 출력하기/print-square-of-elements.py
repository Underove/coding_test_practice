n = int(input())
arr = list(map(int, input().split()))

temp_arr = [x**2 for x in arr]
print(" ".join(map(str, temp_arr)))