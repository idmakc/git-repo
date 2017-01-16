<<<<<<< HEAD
f=open('3-7-5.txt', 'r')
s=f.read().split()
f.close()
l=len(s)
d=[]
c=[]
for i in range(0,l,3):
	d.append(s[i])
print(d)
for i in range(2,l,3):
	c.append(s[i])
print(c)
cnt=0
su=0
for i in range(1, 12):
	if str(i) not in d:
		print(i,'-')
	for j in range(len(d)):
		if i==int(d[j]) and str(i) in d:
			su=su+int(c[j])
			cnt+=1
	if su>0:
		print(i,su/cnt)
	su=0
	cnt=0
=======
n=int(input())
s=[]
for i in range(n):
	s.append(input().split(' '))
#print(s)
'''d={}	
for j in range(n):
	if s[j][0]=='add':
		d[s[j][1]]=s[j][2]
print(d)
'''
r=[]
for j in range(n):
	if s[j][0]=='get':
		for k in range(j):
			if s[k][0]=='add':
				r.append(s[k][1])
				r.append(s[k][2])
			if s[k][0]=='create':
				r.append(s[k][2])
				r.append(s[k][1])
		for z in range(len(r)):
			if s[j][2]==r[z]:
				print(r[z-1])
		if s[j][2] not in r:
			print('None')
		r.reverse()
		print(r)
		r=[]

'''
[['add', 'global', 'a'], ['create', 'foo', 'global'], ['add', 'foo', 'b'], ['get', 'foo', 'a'],
 ['get', 'foo', 'c'], ['create', 'bar', 'foo'], ['add', 'bar', 'a'], ['get', 'bar', 'a'], ['get', 'bar', 'b']]
'''
>>>>>>> master
