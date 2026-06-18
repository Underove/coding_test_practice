A = input()

def palindrome(A):
    for i in range(len(A)):
        if A[:] == A[::-1]:
            return 'Yes'
    return 'No'

print(palindrome(A))