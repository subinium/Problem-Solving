def solution(n):
    if n==0: return ''
    n-=1
    dct = {0:'1', 1:'2', 2:'4'}
    return solution(n//3)+dct[n%3]