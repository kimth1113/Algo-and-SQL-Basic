# 달팽이

def snail(N):
    arr = [[0] * N for _ in range(N)]

    row = 0
    col = -1
    trans = 1
    cnt = 1

    while N > 0:
        for i in range(N):
            col += trans
            arr[row][col] = cnt
            cnt += 1
        N -= 1

        for j in range(N):
            row += trans
            arr[row][col] = cnt
            cnt += 1
        trans *= -1

    return arr

print(snail(5))