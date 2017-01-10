a=int(input())
b=[]
for k in range(a):
	b.append(input().split(';'))
plays=0
win=0
draw=0
lose=0
pts=0
team=dict()
if a==1:
	team[b[0][0]]='0'
	team[b[0][2]]='0'
for i in range(a):
	team[b[i][0]]=''
print(team)
for t in team.keys():
	for i in range(a):
		if t==b[i][0]:
			plays+=1
			if int(b[i][1])>int(b[i][3]):
				win+=1
				pts+=3
			if int(b[i][1])<int(b[i][3]):
				lose+=1
			elif int(b[i][1])==int(b[i][3]):
				draw+=1
				pts+=1
		if t==b[i][2]:
			plays+=1
			if int(b[i][3])>int(b[i][1]):
				win+=1
				pts+=3
			if int(b[i][3])<int(b[i][1]):
				lose+=1
			elif int(b[i][1])==int(b[i][3]):
				draw+=1
				pts+=1
	print(t+':',end='')
	print(plays,win,draw,lose,pts)
	plays=0
	win=0
	draw=0
	lose=0
	pts=0