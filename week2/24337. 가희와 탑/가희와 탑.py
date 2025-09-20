N, a, b = map(int,input().split())

ans = []
if a >= b :
    ans = [i for i in range(1,a+1)] + [i for i in range(b-1,0,-1)]
    if len(ans) < N :
        ans = [1 for _ in range(N-len(ans))] + ans

if a < b :
    ans = [i for i in range(1,a)] + [i for i in range(b,0,-1)]
    if len(ans) < N :
        ans = ans[0:1]+[1 for _ in range(N-len(ans))]+ans[1:]


if len(ans) > N :
    print(-1)
else : 
    print(*ans)