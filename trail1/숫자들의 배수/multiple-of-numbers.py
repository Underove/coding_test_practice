n = int(input())

arr = []
count = 0
i = 1

while True:
    num = n*i
    arr.append(num)
    if num % 5 == 0:
        count += 1
    if count == 2:
        break
    i += 1

print(" ".join(map(str, arr))) 