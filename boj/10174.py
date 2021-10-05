def ck(s):
    return 'Yes' if s == s[::-1] else 'No'


print('\n'.join([ck(input().upper()) for _ in range(int(input()))]))
