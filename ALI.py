import requests as rt
url = 'https://github.com/Aali64/Hs'

rt.get(url)

for i in range(100):
    print(i)
rt.get('https://github.com/Aali64/Hs/blob/main/approval.txt')
