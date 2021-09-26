N = int(input())
answer = [-1 for _ in range(N+1)]


def f(s, n, tot):
    global answer, N
    if tot > N or answer[tot] != -1:
        return

    ch_cnt = [-1 for i in range(n)]
    for idx, ch in enumerate(s, 1):
        chi = ord(ch)-ord('A')
        if ch_cnt[chi] == -1:
            ch_cnt[chi] = idx
        ch_cnt[chi] -= 1

    idx = 0
    s_len = len(s)
    while len(s) != tot:
        while ch_cnt[idx] == 0:
            idx += 1
        ch_cnt[idx] -= 1
        s += chr(ord('A')+idx)

    answer[tot] = s
    for sl in range(len(s), s_len-1, -1):
        f(s[:sl]+chr(ord('A')+n), n+1, tot+sl+1)


f('A', 1, 1)

print(answer[N])
