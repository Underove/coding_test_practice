n = int(input())
arr = list(map(int, input().split()))

temp_arr = [i for i in arr if i % 2 == 0]

print(" ".join(map(str, temp_arr)))

