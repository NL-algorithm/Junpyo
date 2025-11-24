import sys, math

T = int(input())
for t in range(T) :
    N, M = map(int,input().split())
    print(math.comb(M,N))

