n, q = map(int, input().split())
arr = list(map(int, input().split()))

for _ in range(q):
    query = list(map(int, input().split()))
    q_type = query[0]   # 질문 유형

    if q_type == 1:
        a = query[1]
        print(arr[a-1])
    elif q_type == 2:
        b = query[1]
        if b in arr:
            print(arr.index(b) + 1)
        else:
            print(0)
    elif q_type == 3:
        s, e = query[1], query[2]
        print(*arr[s-1:e]) # 잘라낸 구간의 원소들을 공백으로 구분해 출력