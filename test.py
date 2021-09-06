import requests
from bs4 import BeautifulSoup
import pandas as pd

base_url = 'https://www.ava-may.de/collections/blumig'

headers = { 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36 Edg/93.0.961.38'}

r = requests.get(base_url, headers = headers)
soup = BeautifulSoup(r.content, 'html.parser')

container = soup.find_all('div', class_= 'prd-Card')

product_list = []

for item in container:
    name = item.find('h3', class_='prd-Card_Title').text.strip()
    link = 'https://www.ava-may.de/collections/blumig' + item.find('a', class_= 'prd-Card_Link')['href']
    price = item.find('p', class_= 'prd-Card_Price').text.strip()
    
    info = {
        'name' : name,
        'link' : link,
        'price' : price
    }
    product_list.append(info)
print(product_list)

df = pd.DataFrame(product_list)
df.to_excel('ava.xlsx', index= False)
