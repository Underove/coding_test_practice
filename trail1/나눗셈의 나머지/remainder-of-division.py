from collections import defaultdict
A, B = map(int, input().split())
count = defaultdict(int)

while A > 1:
    temp = A % B    # 나머지
    A = A // B      # 몫
    count[temp] += 1

answer = 0
for v in count.values():
    answer += v ** 2
print(answer)
