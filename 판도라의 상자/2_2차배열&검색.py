# 행 우선 순회
for i in range(len(arr)):
    for j in range(len(arr[i])):
        arr[i][j]

# 열 우선 순회
# 열과 행의 수가 같을 때
for j in range(len(arr[0])):
    for i in range(len(arr)):
        arr[i][j]
# 열과 행의 수가 다를 때는 가장 긴 열 구한 후, 실행

# 지그재그 순회 (M * M)
for i in range(len(arr)):
    for j in range(len(arr[0])):
        arr[i][j + (M-1-2*j) * (i % 2)]
              # 앞에 j가 있으니 한번 더 j를 빼줘야함
# 아래와 같음
for i in range(len(arr)):
    for j in range(len(arr[0])):
        if i % 2 == 0:
            arr[i][j]
        else:
            arr[i][M-j-1]

# 전치행렬
for i in range(len(arr)):
    for j in range(len(arr[i])):
        if i < j:
            arr[i][j], arr[j][i] = arr[j][i], arr[i][j]

# 부분집합
bit = [0, 0, 0, 0]
for i in range(2):
    bit[0] = i
    for j in range(2):
        bit[1] = j
        for k in range(2):
            bit[2] = k
            for l in range(2):
                bit[3] = l
                print(bit)

### 보다 간결하게
arr = [3, 5, 6, 1, 5, 4]
N = len(arr)

for i in range(1<<N): # 부분집합의 개수
    for j in range(N):
        if i & (1<<j):
            print(arr[j], end = ' ')
    print()

# 순차검색 (정렬x)
def sequentialSearch(a, n, key):
    i = 0
    while i < n and a[i] != key:
        i += 1
    if i < n: return i
    else: return -1

# 순차검색 (정렬o)
def sequentialSearch2(a, n, key):
    i = 0
    while i < n and a[i] < key:
        i += 1
    if i < n and a[i] == key: return i
    else: return -1

# 이진 검색
def binarySearch(a, key):
    start = 0
    end = len(a) -1
    while start <= end:
        middle = (start + end) // 2
        if a[middle] == key: # 검색 성공
            return true
        elif a[middle] > key:
            end = middle - 1
        else:
            start = middle + 1
    return false



