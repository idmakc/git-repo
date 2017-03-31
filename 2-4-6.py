import os

import re


os.chdir('sample')
#rint(os.getcwd())
L=set()
for root, dirs, files in os.walk('/home/maks/WEB/python2/2/task/sample'):
    if len(files)>0:
    	for i in range(len(files)):
    		if re.findall('.*\.py', files[i]):
    			L.add(root)
print(L)
    #print(currnt_dir, dirs, files)
print(type(root))

#f re.findall('.*\.py', 'hello.py'):
#print('is it')