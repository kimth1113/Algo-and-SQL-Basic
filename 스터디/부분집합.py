# bit = [0,0,0,0]

# for i in range(2):
#     bit[0] = i
#     for j in range(2):
#         bit[1] = j
#         for k in range(2):
#             bit[2] = k
#             for l in range(2):
#                 bit[3] = l
#                 print(*bit)


재료 = ['계란', '치즈', '떡']

N = 3

for i in range(1<<N):
    ans = ''
    for j in range(N):
        if i & (1<<j):
            ans += 재료[j] + ' '

    print(ans,'라면입니다.')