#News2Me.py 
#Created by Bhavdeep Singh as an API Project
#Replace '&' symbols with your own keys

import requests
from Tkinter import *
import webbrowser

root = Tk(className=" NewsReader ")
root.attributes('-alpha', 0.8)
root.config(bg='black')
text = Text(root)
text.config(fg='white', bg='black')
articlelist = []

btcurl = 'https://rest.coinapi.io/v1/exchangerate/BTC/USD'
headers = {'X-CoinAPI-Key' : '&'}
btcrate = requests.get(btcurl, headers=headers)
usdtobtc = (btcrate.json()['rate'])


text.insert(END, "MONEY\n")
text.insert(END, "==================================\n\n")

usdinrurl = requests.get('http://www.apilayer.net/api/live?access_key=&')
usdinrquote = usdinrurl.json()['quotes']['USDINR']
text.insert(END, "USD to INR: ")
text.insert(END, usdinrquote)
text.insert(END, "\n")
text.insert(END, "BTC: ")
text.insert(END, usdtobtc)
text.insert(END, "\n\n")

tcurl = requests.get('https://newsapi.org/v2/everything?sources=techcrunch&apiKey=&')
temp = tcurl.json()['articles']
text.insert(END, "TECH CRUNCH\n")
text.insert(END, "==================================\n\n")

for i in temp[10:]:
    text.insert(END, i['title'])
    text.insert(END, '\n\n')
    text.pack(side = LEFT, fill = BOTH, expand = YES)
    
    
rcurl = requests.get('https://newsapi.org/v2/everything?sources=recode&apiKey=&')
othertemp = rcurl.json()['articles']
text.insert(END, "RECODE\n")
text.insert(END, "==================================\n\n")

for j in othertemp:
    text.insert(END, j['title'])
    text.insert(END, '\n\n')
    text.pack(side = LEFT, fill = BOTH, expand = YES)

hackurl = requests.get('https://newsapi.org/v2/everything?sources=hacker-news&apiKey=&')
thenexttemp = hackurl.json()['articles']
text.insert(END, "HACKER NEWS\n")
text.insert(END, "==================================\n\n")

for i in thenexttemp:
    text.insert(END, i['title'])
    text.insert(END, '\n\n')
    text.pack(side = LEFT, fill = BOTH, expand = YES)

root.update()
root.mainloop()