N = int(input())

buildings = list(map(int,input().split()))
can_see = [0]*N
for i in range(N) :
    maxx = -1000000002
    for j in range(i+1, N) :
        lean = (buildings[i] - buildings[j]) / (i-j)
        if lean > maxx :
            can_see[i] += 1
            maxx = lean

    maxx = 1000000002
    for j in range(i-1, -1, -1) :
        lean = (buildings[i] - buildings[j]) / (i-j)
        if lean < maxx :
            can_see[i] += 1
            maxx = lean
    
print(max(can_see))