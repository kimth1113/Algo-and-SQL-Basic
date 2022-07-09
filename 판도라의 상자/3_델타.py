# 델타 2차 배열
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

for i in range(len(arr)):
    for j in range(len(arr[i])):
        for di in range(4): # 4방향
            testX = i + dx[di]
            testY = j + dy[di]
            test(arr[testX][testY])

# Example
arr = [[1, 2, 3],
       [4, 5, 6],
       [7, 8, 9]]

r = 0
c = 0

# 상하좌우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

for i in range(4):
    nr = r + dr[i]
    nc = c + dc[i]

    if nr < 0 or nr > 2 or nc < 0 or nc > 2: 
       continue # 만약 이렇다면 아무것도 하지마
    else: 
       print(arr[nr][nc])
    # 아래와 같음
    # if 0 <= nr < 3 and 0 <= nc < 3:
    #     print(arr[nr][nc])