<<<<<<< HEAD
<<<<<<< HEAD
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
=======
ok_status=True
vowels=['a', 'u', 'i', 'e', 'o']

def check(word):
	global ok_status
	for vowel in vowels:
		if vowel in word:
			return True
	ok_status=False
	return False

print(check('abacba'))
print(ok_status)
print(check('wwww'))
print(ok_status)
>>>>>>> master
=======
d1 = {}
d1.setdefault('Physics', []).append('Newton')
d1.setdefault('Physics', []).append('Tesla')
print(d1)
print(type(d1))
print(dir(d1))
>>>>>>> master
