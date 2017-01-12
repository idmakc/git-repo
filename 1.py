def create(namespace, variable):
	name.setdefault(namespace,[]).append(variable)
def add(namespace, variable):
	v.setdefault(namespace,[]).append(variable)
def get(namespace, variable):
	if namespace in v.keys():
		print(namespace)
	else:
		if namespace=='global':
			print(None)
		else:
			namespace=name[namespace]
			get(namespace, variable)
name={}
v={}
n=int(input())
for i in range(n):
	cmd,namespace,variable=input().split()
	if cmd=='create':
		create(namespace, variable)
	elif cmd=="add":
		add(namespace, variable)
	elif cmd=='get':
		get(namespace, variable)
print(name)
print(v)
#v={'foo':'b', 'global':'a'}
#name={'foo':'global'}