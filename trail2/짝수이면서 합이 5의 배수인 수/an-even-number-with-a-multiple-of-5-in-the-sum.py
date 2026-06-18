n = int(input())

def solution(n):
    if n % 2 == 0 and (int(str(n)[0]) + int(str(n)[1])) % 5 == 0:
        return "Yes"
    else:
        return "No"

print(solution(n))
