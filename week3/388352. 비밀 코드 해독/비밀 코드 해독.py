def solution(n, q, ans):
    answer = 0
    num = len(ans)
    for i in range(1,n-3) :
        for j in range(i+1,n-2) :
            for k in range(j+1, n-1) :
                for l in range(k+1, n) :
                    for m in range(l+1, n+1) :
                        cur = set([i,j,k,l,m])
                        match = True
                        for a in range(num):
                            set_q = set(q[a])
                            if len(cur & set_q) != ans[a] :
                                match = False
                                break
                        if match :
                            answer += 1
            
    return answer