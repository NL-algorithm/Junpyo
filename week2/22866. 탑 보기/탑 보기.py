import sys
input = sys.stdin.readline

N = int(input().strip())
buildings = list(map(int, input().split()))

right_seen = [-1] * N 
left_seen  = [-1] * N  

stack = []
for i in range(N):
    while stack and buildings[stack[-1]] < buildings[i]:
        idx = stack.pop()
        right_seen[idx] = i
    stack.append(i)

stack = []
for i in range(N-1, -1, -1):
    while stack and buildings[stack[-1]] < buildings[i]:
        idx = stack.pop()
        left_seen[idx] = i
    stack.append(i)

right_chain = [-1 for _ in range(N)]
left_chain  = [-1 for _ in range(N)]

def build_right(i) : 
    if right_chain[i] != -1 : return right_chain[i] 
    if right_seen[i] == -1 : right_chain[i] = 0
    else : right_chain[i] = 1 + build_right(right_seen[i])
    return right_chain[i] 

def build_left(i) : 
    if left_chain[i] != -1 : return left_chain[i] 
    if left_seen[i] == -1 : left_chain[i] = 0
    else : left_chain[i] = 1 + build_left(left_seen[i])
    return left_chain[i]

for i in range(N):
    build_right(i)
    build_left(i)
    seen = left_chain[i] + right_chain[i]

    if left_seen[i] == -1 and right_seen[i] != -1:
        nearest = right_seen[i] + 1
    elif right_seen[i] == -1 and left_seen[i] != -1:
        nearest = left_seen[i] + 1
    else:
        if (i - left_seen[i]) <= (right_seen[i] - i):
            nearest = left_seen[i] + 1
        else:
            nearest = right_seen[i] + 1
    if seen == 0 :
        print(0)
    else :
        print(seen, nearest)
