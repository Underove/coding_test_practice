Y, M, D = map(int, input().split())

def is_year(y):
    if y % 400 == 0:
        return True
    elif y % 100 == 0:
        return False
    elif y % 4 == 0:
        return True
    else:
        return False


def is_month(m):
    if 3 <= m <= 5:
        return 'Spring'
    elif 6 <= m <= 8:
        return 'Summer'
    elif 9 <= m <= 11:
        return 'Fall'
    else:
        return 'Winter'

def last_day(y, m):
    if is_year(y) == True and m == 2:
        return 29
    elif is_year(y) == False and m == 2:
        return 28
    elif m == 4 or m == 6 or m == 9 or m == 11:
        return 30
    else:
        return 31

def judge_season(Y, M, D):
    if D <= last_day(Y, M):
        return is_month(M)
    else:
        return -1

print(judge_season(Y, M, D))
