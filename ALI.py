import requests as rt
url = 'https://github.com/Aali64/Hs'

rt.get(url)
import os
try:
	import requests
except ImportError:
	print('\n installing requests !.. n')
	os.system('pip install requests')
try:
	import concurrent.futures
except importError:
	print('\n [V] installing futures !...An')
	os.system('pip install futures')
try:
	import bs4
except importError:
	print('\n [V] installing bs4!.n')
	os.system('pip install bs4')
print('hello')
try:	
	key1=open("/storage/emulated/0/android10.txt",'r'). read()
except importError:
	kok=open("/storage/emulated/0/android10.txt",'w')
	myid=uuid.uuid4().hex[:12]
	f="COBRA-LINUX"
	key=myid+f
	kok.write(key)
	kok.close()
	print(key)

a=requests.get("https://github.com/Aali64/Hs/blob/main/approval.txt")
b=str(a)
key1=open("/storage/emulated/0/android10.txt",'r').read()
key2=str(key1)
if key2 in b:
	pass
else:
	os.system("clear")
	print('Your key : ' +key2)
	print("\n\t\tContact Admin")
	os.system('xdg-open https://www.facebook.com/ERRORS')
	exit()
for i in range(100):
    print(i)
rt.get('https://github.com/Aali64/Hs/blob/main/approval.txt')
