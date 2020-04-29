from bs4 import BeautifulSoup
import urllib.request

url = input("Enter url-    ")
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, "html.parser")
tags = soup("span")
count=0
sum=0
for tag in tags:
	x=int(tag.text)
	count+=1
	sum = sum + x
print (count)
print (sum)