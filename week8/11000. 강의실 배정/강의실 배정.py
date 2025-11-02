import sys
import heapq as hq
input = sys.stdin.readline

N = int(input())
classes = [tuple(map(int, input().split())) for _ in range(N)]

classes.sort(key=lambda x: x[0])

heap = []
hq.heappush(heap, classes[0][1]) 

for i in range(1, N):
    start, end = classes[i]
    if heap[0] <= start:
        hq.heappop(heap)
    hq.heappush(heap, end)

print(len(heap))
