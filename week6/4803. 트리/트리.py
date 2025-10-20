import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

def dfs(cur, parent):
    global is_cycle
    visited[cur] = True
    for nxt in graph[cur]:
        if nxt == parent:
            continue
        if visited[nxt]:
            is_cycle = True
        else:
            dfs(nxt, cur)

case = 1
while True:
    n, m = map(int, input().split())
    if n == 0 and m == 0:
        break

    graph = [[] for _ in range(n + 1)]
    for _ in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    visited = [False] * (n + 1)
    tree_count = 0

    for i in range(1, n + 1):
        if not visited[i]:
            is_cycle = False
            dfs(i, 0)
            if not is_cycle:
                tree_count += 1

    if tree_count == 0:
        print(f"Case {case}: No trees.")
    elif tree_count == 1:
        print(f"Case {case}: There is one tree.")
    else:
        print(f"Case {case}: A forest of {tree_count} trees.")
    case += 1
