# 레벨2 1954. 달팽이숫자 
import sys
sys.stdin = open("test01.txt", "r")

TC = int(input())
for tc in range(1, TC+1):
    N = int(input())
    arr = [[[0] for _ in range(N)] for _ in range(N)]

    row = 0
    col = -1
    cnt = 1
    tran = 1
    while N > 0:
        for i in range(N):
            col += tran
            arr[row][col] = cnt
            cnt += 1
        N -= 1
        for j in range(N):
            row += tran
            arr[row][col] = cnt
            cnt += 1
        tran *= -1

    print(f"#{tc}")
    for k in range(len(arr)):
        print(*arr[k])