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