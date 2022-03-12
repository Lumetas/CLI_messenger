import sys
import requests

nick = sys.argv[1]
fUrl = input("Ссылка собеседника: ")
start = requests.get(fUrl)
if start:
    print('Connected successfully')
    while True:
        ms = input(nick + ' : ')
        ms = nick + ' : ' + ms
        res = requests.get(fUrl + ms)
else:
    print('ERROR')

    
