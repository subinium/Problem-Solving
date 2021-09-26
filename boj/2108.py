from collections import Counter
numbers = sorted([int(input()) for _ in range(int(input()))])

cnt = Counter(numbers).most_common(2)
print(round(sum(numbers) / len(numbers)))
print(numbers[len(numbers) // 2])
print(cnt[0 if len(numbers) == 1 else cnt[0][1] == cnt[1][1]][0])
print(max(numbers) - min(numbers))
