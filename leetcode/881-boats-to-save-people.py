class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort(reverse=True)
        n = len(people)
        p = n-1
        for i in range(n):
            if i >= p:
                break
            if people[i]+people[p] <= limit:
                p -= 1
        return p+1
