from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import requests


url=requests.get("https://www.billboard.com/charts/hot-100")

soup=BeautifulSoup(url.content,'html.parser')

vec=[]

for link in soup.find_all("div",{"class":"chart-row__main-display"}):
	for linky in link.find_all("span",{"class":"chart-row__current-week"}):
		s_no=linky.text
	for linky in link.find_all("h2",{"class":"chart-row__song"}):
		name=linky.text
	for linky in link.find_all("span",{"class":"chart-row__artist"}):
		artist=linky.text
	for linky in link.find_all("a",{"class":"chart-row__artist"}):
		artist=linky.text
	artist=artist[1:len(artist)-1]
	if artist[len(artist)-1]=='\n':
		artist=artist[:len(artist)-1]
	print(s_no,' ',name,' (',artist,')')
	vec.append((name,artist))

z=int(input("Enter the song number : "))

if z>0 and z<=100:



	s_n=vec[z-1][0]+" "+vec[z-1][1]
	s_n=s_n.replace(" ", "+")
	s_n="https://www.youtube.com/results?search_query="+s_n;


	url=requests.get(s_n)
	soup=BeautifulSoup(url.content,"html.parser")



	for linky in soup.find_all("a",{"class":"yt-uix-tile-link yt-ui-ellipsis yt-ui-ellipsis-2 yt-uix-sessionlink spf-link "}):		
		url=linky.get("href")
		break

	profile = webdriver.FirefoxProfile()
	profile.set_preference("general.useragent.override", "Mozilla/5.0 (X11; Linux x86_64; rv:38.0) Gecko/20100101 Firefox/38.0")
	profile.set_preference("javascript.enabled", True)
	driver = webdriver.Firefox(profile);


	driver.get("https://www.youtube.com"+url)
else:
	print("Invalid Input")

	




	