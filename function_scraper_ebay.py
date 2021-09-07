import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://www.ebay.com/sch/i.html?_from=R40&_nkw=gigabyte+aero+15&_sacat=175672&LH_TitleDesc=0&SSD%2520Capacity=512%2520GB&rt=nc&_oaa=1&_dcat=177'

def get_data(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    return soup

def parse(product_list):
    product_list = []
    results = soup.find_all('div', class_='s-item__info clearfix')
    for item in results:
        products = {
            'title' : item.find('h3', class_='s-item__title').text,
            'Soldprice' : float(item.find_next('span', class_='s-item__price').text.replace('$', '').replace(',', '').strip()),
            'link' : item.find_next('a', class_= 's-item__link')['href']
        }
        product_list.append(products)
    return product_list

def output(product_list):
    productsdf = pd.DataFrame(product_list)
    productsdf.to_excel('anydatascraper.xlsx', index= False)
    print('saved to excel')
    return


soup = get_data(url)
product_list = parse(soup)
output(product_list)





