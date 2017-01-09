n = int(input())
table = {}
for i in range (n):
    strings = input().split(';')
    if strings[0] not in table:
        table [str(strings[0])] = [0, 0, 0, 0, 0]
    if strings[2] not in table:
        table [str(strings[2])] = [0, 0, 0, 0, 0]
    table[strings[0]][0] += 1
    table[strings[2]][0] += 1
    if (int (strings[1])) > (int (strings[3])):
        table[strings[0]][1] += 1
        table[strings[0]][4] += 3
        table[strings[2]][3] += 1
    elif (int (strings[1])) == (int (strings[3])):
        table[strings[0]][2] += 1
        table[strings[0]][4] += 1
        table[strings[2]][2] += 1
        table[strings[2]][4] += 1
    else:
        table[strings[0]][3] += 1
        table[strings[2]][4] += 3
        table[strings[2]][1] += 1
for key in table:
    print (key)
