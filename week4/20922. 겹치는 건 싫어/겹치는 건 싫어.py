N, M = map(int,input().split())
arr = list(map(int,input().split()))

start = 0


count = [0 for _ in range(100001)]


ans = -1 
for i in range(len(arr)) :
    count[arr[i]] += 1 
    if count[arr[i]] > 1 :
        if count[arr[i]] > M :
            while start < i :
                count[arr[start]] -= 1
                start += 1
                if arr[start-1] == arr[i] : 
                    break

    if i-start+1> ans :
        ans = i - start + 1

print(ans)