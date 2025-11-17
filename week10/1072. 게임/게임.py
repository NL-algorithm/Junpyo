import sys
input = sys.stdin.readline

while True:
    line = input().strip()
    if not line:
        break

    X, Y = map(int, line.split())
    Z = (Y * 100) // X

    if Z >= 99:
        print(-1)
        continue

    left, right = 1, 2000000000
    answer = -1

    while left <= right:
        mid = (left + right) // 2
        newZ = ((Y + mid) * 100) // (X + mid)

        if newZ > Z:
            answer = mid
            right = mid - 1
        else:
            left = mid + 1

    print(answer)
