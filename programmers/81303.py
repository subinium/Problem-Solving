def solution(n, k, cmds):
    now = [True for _ in range(n)]
    up, down = [i-1 for i in range(n)], [i+1 for i in range(n)]
    up[0], down[n-1] = None, None
    lst = []
    for cmd in cmds:
        if len(cmd)>1:
            cmd, val = cmd.split()
            val = int(val)
            
        if cmd=='U': 
            for _ in range(val):
                k = up[k]
        elif cmd=='D': 
            for _ in range(val):
                k = down[k]      
        elif cmd=='C':
            lst.append(k)
            now[k] = False
            if up[k]!=None: down[up[k]]=down[k]
            if down[k]: up[down[k]]=up[k]
            k = down[k] if down[k] else up[k]
        elif cmd=='Z': 
            idx = lst.pop()
            now[idx] = True
            if up[idx]!=None: down[up[idx]] = idx
            if down[idx]: up[down[idx]] = idx
        
    return ''.join(['O' if i else 'X' for i in now])