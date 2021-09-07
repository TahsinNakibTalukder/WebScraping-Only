
import requests
from bs4 import BeautifulSoup 
import pandas as pd

headers = { 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36 Edg/93.0.961.38'}

url = 'https://www.ebay.com/sch/i.html?_from=R40&_nkw=sony+a7+iii&_sacat=0&rt=nc&LH_ItemCondition=3000&_pgn=1'




product_list = []
for x in range (1,3):
    r = requests.get(f'https://www.ebay.com/sch/i.html?_from=R40&_nkw=sony+a7+iii&_sacat=0&rt=nc&LH_ItemCondition=3000&_pgn={x}')
    soup = BeautifulSoup(r.content, 'html.parser')

    productlist = soup.find_all('div', class_='s-item__wrapper clearfix')



    for item in productlist:
        name = item.find_next('h3', class_='s-item__title').text.strip()
        price = float(item.find_next('span', {'class': 's-item__price'}).text.replace('$', '').replace(',', '').strip())
        try:
            bid = item.find_next('span', class_ = 's-item__bids s-item__bidCount').text.strip()
        except:
            bid = 'No Bid Available'
        
        container = {
            'name': name,
            'price': price,
            'bid': bid
            }

        product_list.append(container)

    print(product_list)


    df = pd.DataFrame(product_list)
    df.to_excel('ebayscraping.xlsx', index= False)
    


    

