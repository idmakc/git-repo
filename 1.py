f=open('3-7-5.txt', 'r')
s=f.read().split()
f.close()
l=len(s)
d=[]
c=[]
a=[1,2,3,4,5,6,7,8,9,10,11]
for i in range(0,l,3):
	d.append(s[i])
print(d)
for i in range(2,l,3):
	c.append(s[i])
print(c)
cnt=0
su=0
for aEl in a:
	if str(aEl) not in d:
		print(aEl,'-')
	for j in range(len(d)):
		if aEl==int(d[j]) and str(aEl) in d:
			su=su+int(c[j])
			cnt+=1
	if su>0:
		print(aEl,su/cnt)
	su=0
	cnt=0
