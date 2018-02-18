# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import requests, time

urlbase = "https://myanimelist.net"
soup = BeautifulSoup(requests.get("https://myanimelist.net/animelist/3A9IC").content)
animlist = {}
#my_file = open("some1", "w")

#my_file = open("some.txt", "w", encoding='utf-8')
#my_file.write(soup)

#print(str(soup))

b = soup.find('table', "header_completed")

hh= [1,2,3,4,5]
print(hh[3])
#b=soup('table', 'header_completed')
print(b)
Exit = False
co=0
colcicly=0
while not Exit:
	#print('WHWHWWHWHWHWWHWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh')
	b= b.nextSibling
	#print(b)
	
	try:
		bfindTitle = b.find('a', 'animetitle')
		print(bfindTitle['href']," ", bfindTitle.contents[1].contents[0] )
		animlist.update({bfindTitle.contents[1].contents[0]:{
															"url":bfindTitle['href'],
															"Sequel:":"-",
															"Prequel:":"-"
															}})
	except:
		pass
		"""if b is None:
			print("shiet")
		else:
			print(b)"""
	#colcicly+=1
	#print('colcicly= ',colcicly)
	#g = b.find('td', 'category_totals')
	try:
		#co+=1
		#print("WATAFAK", Exit, co)
		if b.find('td', 'category_totals') is not None:
			#co+=1
			#print("4E? ", b.find('td', 'category_totals'))
			Exit = True
			#print("WATAFAK", Exit, co)
		
	except TypeError:
		pass


for eachAnime in animlist:
	#print(animlist[eachAnime]['url'])
	urlF = urlbase + animlist[eachAnime]['url']
	print(urlF)
	soup = BeautifulSoup(requests.get(urlF).content)
	
	time.sleep(1)