import copy

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

cctv = []
sagak = 0
for i in range(N):
    for j in range(M):
        if board[i][j] == 0:
            sagak += 1
        elif 1 <= board[i][j] <= 5:
            cctv.append((i, j, board[i][j]))

dirs = [(-1,0), (0,1), (1,0), (0,-1)]

cctv_dirs = {
    1: [[0], [1], [2], [3]],
    2: [[0,2], [1,3]],
    3: [[0,1], [1,2], [2,3], [3,0]],
    4: [[0,1,2], [1,2,3], [2,3,0], [3,0,1]],
    5: [[0,1,2,3]]
}


def watch(board, y, x, d_idx):
    dy, dx = dirs[d_idx]
    ny, nx = y + dy, x + dx
    count = 0
    while 0 <= ny < N and 0 <= nx < M and board[ny][nx] != 6:
        if board[ny][nx] == 0:
            board[ny][nx] = -1
            count += 1
        ny += dy
        nx += dx
    return count

ans = 100

def backtrack(idx, cur_board, empty):
    global ans

    if idx == len(cctv):
        ans = min(ans, empty)
        return

    y, x, t = cctv[idx]
    for dir_set in cctv_dirs[t]:
        nb = copy.deepcopy(cur_board)
        count = 0
        for d in dir_set:
            count += watch(nb, y, x, d)
        backtrack(idx+1, nb, empty - count)

backtrack(0, board, sagak)
print(ans)
