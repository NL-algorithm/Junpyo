N, M = map(int,input().split())

if M <= N :
    print(N-M) 
else :
    q = [[N,0]]

    ans = abs(M-N)
    visited = [False]*100001
    while q :
        cur, t = q.pop(0)
        if t == ans or visited[cur] :
            continue
        visited[cur] = True
        
        if cur == M :
            ans = t
            break
        nx = cur + 1
        if 0<=nx<=100000 : q.append([nx, t+1])
        nx = cur - 1
        if 0<=nx<=100000 : q.append([nx, t+1])
        nx = cur*2
        if 0<=nx<=100000 : q.append([nx, t+1])


    print(ans)