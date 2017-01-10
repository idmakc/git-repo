n = int(input())
table = {}
for i in range (n):
    strings = input().split(';')
    if strings[0] not in table:
        table [str(strings[0])] = [0, 0, 0, 0, 0]
    if strings[2] not in table:
        table [str(strings[2])] = [0, 0, 0, 0, 0]
print(str(table['ЦСКА'][0]))