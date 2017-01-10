d, s, n = {}, [], int(input())
for i in range(n):
    s.append(input().split(';'))
    if s[i][0] not in d: 
    	d[s[i][0]] = [0] * 5
    if s[i][2] not in d: 
    	d[s[i][2]] = [0] * 5
    if s[i][1] > s[i][3]: 
    	d[s[i][0]][1], d[s[i][2]][3], d[s[i][0]][4] = d[s[i][0]][1] + 1, d[s[i][2]][3] + 1, d[s[i][0]][4] + 3
    if s[i][1] < s[i][3]:
    	d[s[i][2]][1], d[s[i][0]][3], d[s[i][2]][4] = d[s[i][2]][1] + 1, d[s[i][0]][3] + 1, d[s[i][2]][4] + 3
    if s[i][1] == s[i][3]:
    	d[s[i][0]][2], d[s[i][2]][2], d[s[i][0]][4], d[s[i][2]][4] = d[s[i][0]][2] + 1, d[s[i][2]][2] + 1, d[s[i][0]][4] + 1, d[s[i][2]][4] + 1
    d[s[i][0]][0], d[s[i][2]][0] = d[s[i][0]][0] + 1, d[s[i][2]][0] + 1
for key, value in d.items(): print(key + ':' + ' '.join(str(x) for x in value))
