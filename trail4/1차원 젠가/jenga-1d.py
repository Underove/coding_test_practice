n = int(input())
blocks = [int(input()) for _ in range(n)]
# Please write your code here.

array_count = n

def block(s, e):
    global array_count, blocks
    temp = []
    for i in range(array_count):
        if i < s or i > e:
            temp.append(blocks[i])
    array_count = len(temp)
    for i in range(array_count):
        blocks[i] = temp[i]

for _ in range(2):
    s, e = tuple(map(int, input().split()))

    block(s-1, e-1)

print(array_count)
for i in range(array_count):
    print(blocks[i])
    



    