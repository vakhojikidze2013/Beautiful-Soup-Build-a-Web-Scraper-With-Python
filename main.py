import requests
from bs4 import BeautifulSoup
from time import sleep
from random import randint
import csv

f = open('animelist.csv', 'w', newline='\n')
f.write('Title,Category\n')
file_object = csv.writer(f)
file_object.writerow(['Title', 'Category'])
h = {'accept-Language': 'en-US'}
ind = 1
while ind < 6:
    url = f'https://animebest.org/page/{str(ind)}/'
    r = requests.get(url, headers=h)
    content = r.text

    soup = BeautifulSoup(content, 'html.parser')

    main_div_block = soup.find('div', id="dle-content")

    main_class_for_anime = main_div_block.find_all(class_="shortstory")


    for each in main_class_for_anime:

        title = each.h2.a.text
        category = each.find("div", class_="animbest-cat radius-2").a.text
        # print(f'title:{title}')
        # print(f'genre:{category}')
        file_object.writerow([title, category])

    ind += 1
    sleep(randint(10, 20))

print('გილოცავთ თქვენ წარმატებით წამოიღეთ მონაცემები!')