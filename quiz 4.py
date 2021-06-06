import requests
from bs4 import BeautifulSoup
import csv
from time import sleep
from random import randint

url_p = {'genres':'animation','start':1}
url = 'https://www.imdb.com/search/title/'
h = {'Accept-Language':'en-US'}
file = open('imdbanimation.csv', 'w', newline='\n')
file_obj = csv.writer(file)
file_obj.writerow(['Title', 'Year'])

while url_p['start']<=201:
    r = requests.get(url, params=url_p, headers=h)
    content = r.text
    soup = BeautifulSoup(content, 'html.parser')
    movie_block = soup.find('div', class_='lister-list')
    # print(movie_block)
    all_movies = movie_block.find_all('div', class_= 'lister-item')
    for each in all_movies:
        title = each.h3.a.text
        year = each.find('span', class_='lister-item-year').text
        year = year.replace('(','')
        year = year.replace(')','')
        file_obj.writerow([title, year,])
        print(title)

    url_p['start'] += 50
    sleep(randint(10,15))








