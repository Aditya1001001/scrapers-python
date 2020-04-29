import urllib.request
from bs4 import BeautifulSoup
url = input('Enter url-     ')
count = int(input("Enter count-    "))
position = int(input("Enter position-    "))
while count:
    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html, "html.parser")

    tags = soup('a')
    s = []
    t = []
    for tag in tags:
        x = tag.get('href', None)
        s.append(x)
        y = tag.text
        t.append(y)
    
    print (s[position-1])
    print (t[position-1])
    url = s[position-1]
    count-=1