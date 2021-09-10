import requests
from bs4 import BeautifulSoup
import pandas as pd


propertyInfo = []


for x in range(1,50):
    url = 'https://www.discudemy.com/language/English/'
    r = requests.get(url + str(x))
    soup = BeautifulSoup(r.content, 'html.parser')
    content = soup.find_all('div', class_='content')
    # print(len(content))


    for property in content:
        try:
            title = property.find_next('div', class_='header').text
        except:
            title = 'NONE'
        try:
            link = property.find_next('div', class_='header').find('a')['href']
        except:
            link = 'NO LINK'
        try:
            description = property.find_next('div', class_='description').text.strip()
        except:
            description = 'NO DESCRIPTION'
        
        info = {
            'title' : title,
            'link' : link,
            'description' : description
        }
        propertyInfo.append(info)
    print(propertyInfo)


df = pd.DataFrame(propertyInfo)
df.to_excel('udemyfreecourseslist.xlsx', index = False)






