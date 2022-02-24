class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0:
            return '0'
        pm = 1
        answer = ''
        if num < 0:
            num, pm = -num, -1
        while num:
            answer += str(num % 7)
            num //= 7
        return '-'*(pm == -1)+answer[::-1]
