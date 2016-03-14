import os
import requests
from bs4 import BeautifulSoup

name = input("Enter Movie name")
name.replace(" ","")
# name = "triangle"
url = "http://www.imdb.com/find?ref_=nv_sr_fn&q="+name+"&s=all"
sc = requests.get(url)
soup = BeautifulSoup(sc.text,'html.parser')

map = {}

for res in soup.find_all('td',{'class':'result_text'}):
    link  = res.find('a')['href']
    map[res.get_text()] = link
    # print(link)
    # print(res.get_text())


i = 1
for key, value in map.items():
    print(str(i)+" "+key)
    i = i+1;



index = int(input("Enter the index"))
url_1 = 'http://www.imdb.com'+str(list(map.values())[(index-1)])
# print(url_1)
sc_1 = requests.get(url_1)
soup = BeautifulSoup(sc_1.text,'html.parser')

for div in soup.find_all('div',{'class':'ratingValue'}):
    rating = div.find('span')
    print("Rating of this Movie/Tv series is :"+rating.get_text())
print("Summary")

for div in soup.find_all('div',{'class':'plot_summary'}):
    summary = div.find('div',{'class':'summary_text'},{'itemprop':'description'})
    print(summary.text.lstrip())
    director = div.find('span',{'class':'itemprop'},{'itemprop':'name'})
    print("Director is "+director.text)

print("Actors are ")

for div in soup.find_all('span',{'itemprop':'actors'}):
    actors = div.find('span')
    print(actors.get_text())





# print(url_1)
# print(map)

# print(soup)