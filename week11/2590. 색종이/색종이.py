arr = []
for _ in range(6):
    arr.append(int(input()))

ans = 0

one, two, three, four, five, six = arr  #

# 6x6
ans += six

# 5x5
ans += five
one = max(0, one - 11 * five)  

# 4x4
ans += four
need_2x2 = four * 5  
if two >= need_2x2:
    two -= need_2x2
else:
    missing = need_2x2 - two  
    one = max(0, one - missing * 4)  
    two = 0

# 3x3
ans += (three + 3) // 4
rem = three % 4

if rem == 1:
    if two >= 5:
        two -= 5
        one = max(0, one - 7)
    else:
        need = 5 - two
        one = max(0, one - (need * 4 + 7))
        two = 0
elif rem == 2:
    if two >= 3:
        two -= 3
        one = max(0, one - 6)
    else:
        need = 3 - two
        one = max(0, one - (need * 4 + 6))
        two = 0
elif rem == 3:
    if two >= 1:
        two -= 1
        one = max(0, one - 5)
    else:
        one = max(0, one - 9)

# 2x2
ans += (two + 8) // 9 
r2 = two % 9
if r2 != 0:
    one = max(0, one - (36 - r2 * 4))

# 1x1
ans += (one + 35) // 36 

print(ans)
