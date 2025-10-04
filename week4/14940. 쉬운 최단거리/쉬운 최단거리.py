N, M = map(int,input().split())
board = []
start = [-1,-1]
ans = [[-1 for _ in range(M)] for _ in range(N)]
for i in range(N) :
    board.append(list(map(int,input().split())))
    for j in range(M) :
        if board[i][j] == 2 :
            start = [i,j]
        if board[i][j] == 0 :
            ans[i][j] = 0

q = []
q.append([start[0], start[1], 0])
visited = [[False for _ in range(M)] for _ in range(N)]


while q :
    y, x, dist = q.pop(0)
    if visited[y][x] : continue
    visited[y][x] = True
    ans[y][x] = dist

    for dy, dx in [(-1,0), (1,0), (0,-1), (0,1)] :
        ny, nx = y+dy, x+dx
        if 0<=ny<N and 0<=nx<M and board[ny][nx] == 1 :
            q.append([ny,nx,dist+1])

for i in range(N) :
    print(*ans[i])