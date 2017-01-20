def create(namespace, variable):
	name.setdefault(namespace,[]).append(variable)
def add(namespace, variable):
	v.setdefault(namespace,[]).append(variable)
def get(namespace, variable):
	if namespace in v.keys():
		if variable in v[namespace]:
			print(namespace)
		elif namespace=='global':
			print(None)
		else:	
			namespace=name[namespace]
			namespace=namespace[0]
			#print(type(namespace))
			get(namespace, variable)
	
	#else:
		#print(None)
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
print('name:', name)
print('v:', v)
#name={'bar': ['foo'], 'foo': ['global']}
#v={'global': ['a'], 'bar': ['a'], 'foo': ['b']}
6
create foo global
create bar foo
add bar b
create zoo bar
create doo zoo
get zoo b
