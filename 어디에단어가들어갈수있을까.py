# 레벨2 1979. 어디에 단어가 들어갈 수 있을까
import sys
sys.stdin = open("test01.txt", "r")


TC = int(input())
for tc in range(1, TC+1):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    total = 0
    for i in range(N):
        cnt_R = 0
        cnt_C = 0
        for j in range(N):
            if arr[i][j]:
                cnt_R += 1
            elif cnt_R == K and arr[i][j] == 0:
                total += 1
                cnt_R = 0
            else:
                cnt_R = 0
            if arr[j][i]:
                cnt_C += 1
            elif cnt_C == K and arr[j][i] == 0:
                total += 1
                cnt_C = 0
            else:
                cnt_C = 0
        if cnt_C == K: total += 1
        if cnt_R == K: total += 1


    print(f"#{tc} {total}")
