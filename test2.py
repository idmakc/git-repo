<<<<<<< HEAD
s=['8', 'Bishop', '166', '10', 'Waller', '173', '9', 'Andrews', '166']
for i in range(5):
	s2=s.pop(i)
print(s)
=======
n, k = map(int, input().split())
def C(x, y):
    if y == 0:
        return 1
    if y > x:
        return 0
    return C(x - 1, y) + C(x - 1, y - 1)
print(C(n, k))
>>>>>>> master
