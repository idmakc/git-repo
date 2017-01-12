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
