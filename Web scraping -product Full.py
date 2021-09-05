import requests
from bs4 import BeautifulSoup
import pandas as pd

baseurl= 'https://www.thewhiskyexchange.com/'

header = {
    'User-Agent'= 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36'
}

 # creating a blank list for storing product links
productlinks = []
# we used the f string to loop through all the pages. Because it is a javascript site. Requests can not call the next pages if it is written with javascript. Then u have to use f string to loop through the next pages.
for x in range(1,6):
    r = requests.get(f'https://www.thewhiskyexchange.com/c/35/japanese-whisky?pg={x}&psize=24&sort=pasc')
    soup = BeautifulSoup(r.content, 'lxml')
    ## finding all the product containers which carries the links images and ratings of the product
    productlist = soup.find_all('li', class_='product-grid__item')
    # print(productlist)
 
    # Now looping to find all the links (basically this loop is looking inside of all items in productlist and again looping to find all the a tags and hrefs out of it)
    for item in productlist:
        for link in item.find_all('a', href=True):
            # print(link['href'])
            productlinks.append(baseurl + link['href'])
print(productlinks)

# finding product details with a test link

# testlink = 'https://www.thewhiskyexchange.com/p/23772/yamazaki-distillers-reserve'

whiskylist = []
for link in productlinks:
    r = requests.get(link)
    soup = BeautifulSoup(r.content, 'lxml')

    name = soup.find('h1', class_='product-main__name').text.strip()
    price = soup.find('p', class_= 'product-action__price').text.strip()
    try:
        rating = soup.find('span', class_='review-overview__rating star-rating star-rating--45').text.strip()
    except:
        rating = 'no rating'
    # review = soup.find('span', class_='review-overview__count').text.strip()
    
    # print(name,rating,price, review)
    whisky = {
        'name': name,
        'rating': rating,
        # 'review': review,
        'price' : price
        }

    whiskylist.append(whisky)
    print('saving: ', whisky['name'])
# create a dataframe to store all the datas from the dictionary to later export as csv or excel file
df = pd.DataFrame(whiskylist)
# print(df.head(30))

df.to_excel ('test1.xlsx', index= False)