import urllib.request
from bs4 import BeautifulSoup 
import csv

def hexToRGB(hex):
    hex = hex.upper()
    R = hex[0:2]
    G = hex[2:4]
    B = hex[4:]
    hex_dict = {"0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7,
                "8": 8, "9": 9, "A": 10, "B": 11, "C": 12, "D": 13, "E": 14, "F": 15}

    return int(hex_dict[R[0]]*16+hex_dict[R[1]]), int(hex_dict[G[0]]*16+hex_dict[G[1]]), int(hex_dict[B[0]]*16+hex_dict[B[1]])


URL = "https://www.december.com/html/spec/colorhex.html"
response = urllib.request.urlopen(URL)
html = response.read()
soup = BeautifulSoup(html, "html.parser") 
tags = soup('th')
# print(len(tags))
with open('colors.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    for i in range(len(tags)):
        content = tags[i].text
        if content[0] == "#":    
            R, G, B = hexToRGB(content[1:])
            writer.writerow([str(tags[i-1].text), str(content), R, G, B])