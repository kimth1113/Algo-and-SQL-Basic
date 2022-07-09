arr = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
    ]

r = 0
c = 1
N = 3

# 상하좌우
dr = [-1,1,0,0]
dc = [0,0,-1,1]
# 상하좌우
drc = [[-1,0], [1,0], [0,-1], [0,1]]

for i in range(4):
    nr = r+dr[i]
    nc = c+dc[i]

    # 범위에서 벗어나면 제어
    # if nr < 0 or nr >= N or nc < 0 or nc>=: continue
    # print(arr[nr][nc])
    # 아래와 같음
    if 0<=nr<N and 0<=nr<N:
        print(arr[nr][nc])