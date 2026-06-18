M, D = map(int, input().split())

def day_count(M):
    if M == 2:
        return 28
    elif M == 4 or M == 6 or M == 9 or M == 11:
        return 30
    else:
        return 31

def is_true(M, D):
    if M <= 12 and D <= day_count(M):
        return 'Yes'
    else:
        return 'No'

print(is_true(M, D))