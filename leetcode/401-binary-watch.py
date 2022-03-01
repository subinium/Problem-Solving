class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        answer = []
        for h in range(12):
            for m in range(60):
                cnt = (str(bin(h))+str(bin(m))).count('1')
                if cnt == turnedOn:
                    answer.append(f'{h}:{m:02}')
        return answer
