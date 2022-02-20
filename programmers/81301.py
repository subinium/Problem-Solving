# https://programmers.co.kr/learn/courses/30/lessons/81301
def solution(s):
    dct = ['zero', 'one', 'two', 'three', 'four',
           'five', 'six', 'seven', 'eight', 'nine']
    for num, eng in enumerate(dct):
        s = s.replace(eng, str(num))
    return int(s)
