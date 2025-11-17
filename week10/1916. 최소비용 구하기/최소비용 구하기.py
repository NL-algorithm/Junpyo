import sys
import heapq

input = sys.stdin.readline

N = int(input())
M = int(input())

graph = [[] for _ in range(N + 1)]

for _ in range(M):
    s, e, cost = map(int, input().split())
    graph[s].append((e, cost))

start, end = map(int, input().split())

INF = float('inf')
dist = [INF] * (N + 1)
dist[start] = 0

heap = [(0, start)]

while heap:
    current_cost, now = heapq.heappop(heap)

    if dist[now] < current_cost:
        continue
    
    for nxt, cost in graph[now]:
        new_cost = current_cost + cost
        if new_cost < dist[nxt]:
            dist[nxt] = new_cost
            heapq.heappush(heap, (new_cost, nxt))

print(dist[end])
