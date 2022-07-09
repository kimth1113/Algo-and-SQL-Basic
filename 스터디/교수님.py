arr = [[1, 2, 3], [2, 3, 4], [3, 4, 5], [4, 5, 6]]

# 첫번째 행의 데이터를 출력
# 1
for r in range(4):
    print(*arr[r])
# 2
for i in range(4):
    for i in range(3):
        print(arr[r][i], end=' ')
    print()

# 첫번째 열의 데이터를 출력
for c in range(3):
    for j in range(4):
        print(arr[i][c], end = ' ')
    print()

# 전체의 합을 구해라
value = 0
for r in range(4)
    for i in range(3):
        value += arr[r][i]
print(value)

# 각 행의 합을 구해 합이 제일 큰 행의 값을 출력해라
maxV = 0
maxP = 0
for r in range(4):
    value = 0
    for c in range(3):
        value += arr[r][c]
    print(value)
    if maxV < value:
        maxV = value
        maxP = r
print(maxP, maxV)

# 각 열의 합을 구해 합이 제일 큰 행의 값을 출력해라
maxV = 0
maxP = 0
for c in range(3):
    value = 0
    for r in range(4):
        value += arr[r][c]
    print(value)
    if maxV < value:
        maxV = value
        maxP = r
print(maxP, maxV)
