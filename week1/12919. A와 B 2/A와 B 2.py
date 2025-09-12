S = list(input())
T = list(input())

q = [T]

ans = False
while q :
    t = q.pop()
    if len(t) == len(S) :
        if t == S : 
            ans = True 
            break
        continue
    if t[-1] == 'A' :
        q.append(t[0:len(t)-1])
        
    if t[0] == 'B' :
        t.reverse()
        t.pop()
        q.append(t)


if ans :
    print(1)
else :
    print(0)
