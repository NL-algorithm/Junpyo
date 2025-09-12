N = int(input())
M = int(input())

link = []
for i in range(N) :
    link.append(list(map(int,input().split())))

group = [i for i in range(N)]
visited = [False]*N
for i in range(N) :
    if group[i] != i : continue
    visited[i] = True
    q = [i]
    while q :
        cur = q.pop()
        for j in range(N) :
            if link[cur][j] == 1 and not visited[j] :
                visited[j] = True
                q.append(j)
                group[j] = i

plan = list(map(int,input().split()))
ans = "YES"
g = -1
for city in plan :
    if g == -1 : g = group[city-1]
    if group[city-1] != g :
        ans = "NO"
        break
print(ans)