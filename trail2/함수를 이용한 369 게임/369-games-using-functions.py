a, b = map(int, input().split())

def contain_3(n):
    for j in range(0, len(str(n))):
        if str(n)[j] == '3' or str(n)[j] == '6' or str(n)[j] == '9':
            return True
    return False

count = 0 
for i in range(a, b+1):
    if i % 3 == 0 or contain_3(i):
        count += 1

print(count)