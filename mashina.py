import requests
import csv
from bs4 import BeautifulSoup as BS
price = []
def get_html(url):
    responce = requests.get(url)
    return responce.text

def get_soup(html):
    soup = BS(html,'lxml')
    return soup

def get_data(soup):
    cars = soup.find_all('div',class_="list-item list-label")
    
   
    for car in cars:
        try:
            model = car.find('div', class_="block title").text.strip()
        except AttributeError:
            model = None
        try:    
            price = car.find('div',class_="block price").find('strong').get_text(strip=True)
        except AttributeError:
            price = None
        try:  
            img = car.find('div', class_='thumb-item-carousel').find('img', class_='lazy-image').get('data-src')
        except AttributeError:
            img = None      
        try:    
            info = car.find('div' , class_="info-wrapper").get_text(strip=True)
        except AttributeError:
            info = None    
        write_csv({
            'car' : model,
            'price' : price,
            'image': img,
            'info': info    
            })    
            

            
        
def write_csv(data):
    with open('cars.csv', 'a') as file:
        names = ['car','price', 'image','info']
        write = csv.DictWriter(file,delimiter=';', fieldnames = names)  
        write.writerow(data)   

def main():
    for i in range(1,10):
        url = f'https://www.mashina.kg/search/all/?page={i}'
        print(f'спарсили {i} - ую страницу')
        html = get_html(url)
        soup = get_soup(html)
        get_data(soup)
main()

#





