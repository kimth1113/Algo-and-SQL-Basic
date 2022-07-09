arr = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [10, 11, 12, 13]
    ]

N = 3 # 행의 길이
M = 4 # 열의 길이
# len(arr) # 행의 길이
# len(arr[0]) # 열의 길이

# 행 우선 순회
# for i in range(N):
#     for j in range(M):
#         print(arr[i][j])

# 행 우선 순회를 역으로 돌아보자
# for i in range(N):
#     for j in range(M-1, -1, -1):
#         print(arr[i][j])

# 열 우선 순회 
# for j in range(len(arr[0])):
#     for i in range(len(arr)):
#         print(arr[i][j])

# 열 우선 순회를 역으로
# for j in range(M):
#     for i in range(N-1, -1, -1):
#         print(arr[i][j])

# 지그재그
# for i in range(len(arr)):
#     for j in range(len(arr[0])): 
#         print(arr[i][j + (M-1-2*j) * (i%2)])
# if문으로 만드는 지그재그도 학습하기

# 대각선, 달팽이도 공부해보기

