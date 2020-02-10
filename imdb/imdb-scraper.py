import urllib.request
from bs4 import BeautifulSoup 
import csv

def commasToInt(string):
    strings = string.split(",")
    s = ''
    for x in strings:
        s+=x
    return (int(s))


URL = "https://www.imdb.com/chart/top/"
response = urllib.request.urlopen(URL)
html = response.read()
soup = BeautifulSoup(html, "html.parser") 
title_and_year = soup.find_all('td', "titleColumn")
ratings = soup.find_all('td', "ratingColumn imdbRating")
x = len(ratings)
with open('imdb.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    # adding the headers
    writer.writerow(["Title", "Year", "link" , "Cast & Director", "Rating", "Number of reviews"])

    for i in range(x):
        # processing the title column
        a = title_and_year[i].find("a")
        span = title_and_year[i].find("span")
        title = str(a.contents[0])
        link = "https://www.imdb.com" + a.get('href')  
        year = int(str(span.contents[0])[1:-1])
        cast_info =  a.get('title')
        # processing the rating column
        strong = ratings[i].find("strong")
        rating = strong.get('title')  
        processed_title = rating.split(" ")
        no_of_reviews = commasToInt(processed_title[3])
        rate = float(processed_title[0])
        # writing to file
        writer.writerow([title, year, link, cast_info, rate, no_of_reviews])
        # print(title, year, link, cast_info, rate, no_of_reviews, sep = "  ")