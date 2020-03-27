n = int(input())
n1 = n // 50
n2 = (n % 50) // 30
n3 = (n - (50 * n1 + 30 * n2)) / 10
n4 = 7 * n1 + 4 * n2 + n3
print(int(n4))
