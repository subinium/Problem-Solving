S = input()

for idx, alp in enumerate('ABC'):
    if alp in S:
        for alp2 in 'BCDF'[idx:]:
            S = S.replace(alp2, alp)
        break
else:
    S = 'A'*len(S)

print(S)
