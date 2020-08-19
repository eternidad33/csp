def xiaoChuLeiYouXi(A, n, m):
    # B中元素为1，代表在A中连续
    B = [[0] * m for _ in range(n)]
    global i
    for i in range(n):
        for j in range(m):
            # 竖排三个相同
            if 0 < i < n - 1 and A[i - 1][j] == A[i][j] and A[i][j] == A[i + 1][j]:
                B[i - 1][j] = 1
                B[i][j] = 1
                B[i + 1][j] = 1
            # 横排三个相同
            if 0 < j < m - 1 and A[i][j - 1] == A[i][j] and A[i][j] == A[i][j + 1]:
                B[i][j - 1] = 1
                B[i][j] = 1
                B[i][j + 1] = 1
    for i in range(n):
        for j in range(m):
            if B[i][j] == 1:
                A[i][j] = 0
            print(A[i][j], end=" ")
        print()


n, m = map(int, input().split())
lm = []
for i in range(n):
    lm.append(list(map(int, input().split())))
xiaoChuLeiYouXi(lm, n, m)
'''
4 5
2 2 3 1 2
3 1 1 1 1
2 3 2 1 3
2 2 3 3 3
'''
