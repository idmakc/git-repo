n, k = map(int, input().split())
def C(x, y):
    if y == 0:
        return 1
    if y > x:
        return 0
    return C(x - 1, y) + C(x - 1, y - 1)
print(C(n, k))
