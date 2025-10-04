N, M = map(int,input().split())
board = [-1 for _ in range(101)]
for i in range(N+M) :
    a, b = map(int,input().split())
    board[a] = b

minn = 100000000
q = []
q.append([1,0])

visited = [False]*101
while q :
    cur, trial = q.pop(0)
    if cur >= 100 :
        minn = min(trial, minn)
        continue

    if visited[cur] : continue
    visited[cur] = True

    for i in range(1, 7) :
        next = cur + i
        while next < 100 and board[next] != -1 :
            next = board[next]
        q.append([next, trial+1])


print(minn)
        

