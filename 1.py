f=open('3-7-5.txt', 'r')
s=f.read().split()
f.close()
l=len(s)
print(s)
d=[]
c=[]
cnt1,cnt2,cnt3,cnt4,cnt5,cnt6,cnt7,cnt8,cnt9,cnt10,cnt11=0
su1,su2,su3,su4,su5,su6,su7,su8,su9,su10,su11=0
#for i in range(l):
#	if s[i]=='1'
#		cnt1+=1


for i in range(0,l,3):
	d.append(s[i])
print(d)
for i in range(2,l,3):
	c.append(s[i])
print(c)

for i in range(len(d)):
	if '1'==d[i]:
		cnt1+=1
		su1=su1+int(c[i])
	if '2'==d[i]:
		cnt2+=1
		su2=su2+int(c[i])
	if '3'==d[i]:
		cnt3+=1
		su3=su3+int(c[i])	
	if '4'==d[i]:
		cnt4+=1
		su4=su4+int(c[i])
	if '5'==d[i]:
		cnt5+=1
		su5=su5+int(c[i])
	if '6'==d[i]:
		cnt6+=1
		su6=su6+int(c[i])
	if '7'==d[i]:
		cnt7+=1
		su7=su7+int(c[i])
	if '8'==d[i]:
		cnt8+=1
		su8=su8+int(c[i])	
	if '9'==d[i]:
		cnt9+=1
		su9=su9+int(c[i])
	if '10'==d[i]:
		cnt10+=1
		su10=su10+int(c[i])
	if '11'==d[i]:
		cnt11+=1
		su11=su11+int(c[i])
print('1'+su1/cnt1)
print('2'+su2/cnt2)
print('3'+su3/cnt3)
print('4'+su4/cnt4)
print('5'+su5/cnt5)
print('6'+su6/cnt6)
print('7'+su7/cnt7)
print('8'+su8/cnt8)
print('9'+su9/cnt9)
print('10'+su10/cnt10)
print('11'+su11/cnt11)






	
