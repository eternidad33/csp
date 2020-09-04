defaback = [0, 0, 0]
reset = "[0m"
last = []
s = ""
prefix = "\\x1B"


def solveCol(c):
    if len(c) == 2:
        c += c[-1] * 6
    elif len(c) == 4:
        c = "#" + c[1] * 2 + c[2] * 2 + c[3] * 2
    l = [int(c[i:i + 2], 16) for i in range(1, 7, 2)]
    return l


m, n = map(int, input().split())
p, q = map(int, input().split())
colormatrix = [[] for i in range(n)]
for row in range(n):
    for col in range(m):
        colormatrix[row].append(solveCol(input()))
        if (col + 1) % p == 0 and (row + 1) % q == 0:
            srow = row // q
            scol = col // p
            suit = list(
                zip(*[colormatrix[k][l] for l in range(col - p + 1, col + 1) for k in range(row - q + 1, row + 1)]))

            current = [sum(s) // len(s) for s in suit]

            if srow == 0 and scol == 0:
                if current != defaback:
                    d = "[48;2;" + ";".join(map(str, current)) + "m"
                    t = ["\\x" + hex(ord(i))[2:].upper().zfill(2) for i in d]
                    s += prefix + "".join(t)
            else:
                if current == last:
                    pass
                else:
                    if current == defaback:
                        s += "\\x1B\\x5B\\x30\\x6D"
                    else:
                        d = "[48;2;" + ";".join(map(str, current)) + "m"

                        t = ["\\x" + hex(ord(i))[2:].upper().zfill(2) for i in d]
                        s += prefix + "".join(t)
            last = current
            # 空格
            s += "\\x20"
            # 换行
            if scol == m // p - 1:
                # 输出每行后判断是否重置
                if last != defaback:
                    s += "\\x1B\\x5B\\x30\\x6D"
                    last = defaback

                s += '''\\x0A'''
print(s)
