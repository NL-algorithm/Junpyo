def solution(n):
    answer = 0
    
    dp = [[-1 for _ in range(2*n)] for _ in range(2*n)]

    def cal(stack, length) :
        if dp[stack][length] != -1 :
            return dp[stack][length]
        if stack == 0 :
            return cal(stack+1,length+1)
        if length == 2*n and stack == 0 :
            return 1
        if length + stack == 2*n :
            return 1
        if length + stack > 2*n :
            return 0
        
        dp[stack][length] = 0
        if stack > 0 :
            dp[stack][length] += cal(stack-1, length+1)
        dp[stack][length] += cal(stack+1, length+1)
        return dp[stack][length]
    
    return cal(0,0)