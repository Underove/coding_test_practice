A = input()

def solution(A):
    sum = 0
    for i in range(len(A)):
        for j in range(len(A)):
            if A[i] != A[j]:
                sum += 1
    if sum > 0:
        return 'Yes'
    else:
        return 'No'

print(solution(A))