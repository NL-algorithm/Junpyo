
N, K = map(int,input().split())
temp = list(map(int,input().split()))
A = []
for i in temp :
    A.append([i, 0])
A1 = A[-N-1:-2*N-1:-1]
A2 = A[N:2*N]
A2.reverse()


c = 0
step = 0
def down() :
    if A1[0][1] == 1 : A1[0][1] = 0

while c < K :
    step += 1

    # 한칸 회전한다
    A2.append(A1.pop(0))
    A1.append(A2.pop(0))
    down()

    # 회전할 수 있다면 이동한다
    for i in range(1, N) :
        if A1[i][1] == 1 and A1[i-1][1] == 0 and A1[i-1][0] > 0 :
            A1[i][1] = 0
            A1[i-1][1] = 1
            A1[i-1][0] -= 1
            if A1[i-1][0] == 0 :
                c += 1
    down()

    # 올릴 수 있으면 올린다
    if A1[-1][0] > 0 and A1[-1][1] == 0:
        A1[-1][1] = 1
        A1[-1][0] -= 1
        if A1[-1][0] == 0 :
            c += 1

    # print(A1[::-1])
    # print(A2)
    # print(c)
    # print()

    
    
print(step)