def count_bits(x):
    return bin(x).count('1')

N, K = map(int, input().split())

if K >= N:     
    print(0)

else : 

    cnt = 0
    while count_bits(N) > K:
        N += 1
        cnt += 1
    print(cnt)
