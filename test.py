'''
d, s, n = {}, [], int(input())
for i in range(n):
    s.append(input().split(';'))
    if s[i][0] not in d: d[s[i][0]] = [0] * 5
    if s[i][2] not in d: d[s[i][2]] = [0] * 5
    if s[i][1] > s[i][3]: d[s[i][0]][1], d[s[i][2]][3], d[s[i][0]][4] = d[s[i][0]][1] + 1, d[s[i][2]][3] + 1, d[s[i][0]][4] + 3
    if s[i][1] < s[i][3]: d[s[i][2]][1], d[s[i][0]][3], d[s[i][2]][4] = d[s[i][2]][1] + 1, d[s[i][0]][3] + 1, d[s[i][2]][4] + 3
    if s[i][1] == s[i][3]: d[s[i][0]][2], d[s[i][2]][2], d[s[i][0]][4], d[s[i][2]][4] = d[s[i][0]][2] + 1, d[s[i][2]][2] + 1, d[s[i][0]][4] + 1, d[s[i][2]][4] + 1
    d[s[i][0]][0], d[s[i][2]][0] = d[s[i][0]][0] + 1, d[s[i][2]][0] + 1
for key, value in d.items(): print(key + ':' + ' '.join(str(x) for x in value))
'''


n,tt=int(input()),{}
def upd(dic, key, value):
    if key in dic:   dic[key]=list(map(lambda x,y:x+y,dic[key],value))
    else:            dic[key]=value
for k in range(0,n):
    coma,an,comb,bn=input().split(';')
    if    int(an)>int(bn):    a=upd(tt, coma, [1,1,0,0,3]),upd(tt, comb, [1,0,0,1,0])
    elif  int(an)==int(bn):   a=upd(tt, coma, [1,0,1,0,1]),upd(tt, comb, [1,0,1,0,1])
    else:                     a=upd(tt, coma, [1,0,0,1,0]),upd(tt, comb, [1,1,0,0,3])
for key in tt:print(key+":"+' '.join([str(k) for k in tt[key]]))