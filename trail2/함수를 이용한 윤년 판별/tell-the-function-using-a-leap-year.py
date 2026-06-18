y = int(input())

def is_year(y):
    if y % 4 == 0:
        if y % 100 == 0 and y % 400 != 0:
            return 'false'
        else:
            return 'true'
    else:
        return 'false'

print(is_year(y))