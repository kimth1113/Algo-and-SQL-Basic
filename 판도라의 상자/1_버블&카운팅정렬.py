# 버블정렬
def Bubble_sort(arr):
    for i in range(len(arr)-1, 0, -1):
        for j in range(0, i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

# 카운팅 정렬
original = [5, 0, 1, 1, 4, 3, 1, 4, 5, 2, 1]

counting = [0] * 6
for i in range(len(original)):
    counting[original[i]] += 1

for i in range(1, len(counting)):
    counting[i] += counting[i-1]

result = [0] * len(original)
for i in original:
    result[counting[i]-1] = i
    counting[i] -= 1