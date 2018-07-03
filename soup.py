from bs4 import BeautifulSoup
import requests

import csv

import pandas as pd


base_url ='https://www.daraz.com.bd/phones-tablets/?special_price=1'

total_page =25



# with open('simple.html') as html_file:
#     soup = BeautifulSoup(html_file,'lxml')

# # print(soup.prettify())

# # title = soup.body.h1.text

# # print(title)

# for article in soup.find_all('div',class_='article'):
#     title = article.h2.a.text
#     body = article.p.text
#     print(title)
#     print(body)
#     print()

output = []

def make_csv(url):
    source = requests.get(url).text
    soup = BeautifulSoup(source,'lxml')

    for container in soup.find_all('div',class_='sku -gallery '):

        image1 = container.find('div',class_='image-wrapper default-state').img['data-src']
        brand = container.find('h2',class_='title').find('span',class_='brand').text.strip()

        name = container.find('h2',class_='title').find('span',class_='name').text.encode("ascii","ignore").decode('utf-8')
        new_price = container.find('div',class_='price-container clearfix')\
            .find('span',class_='price-box').find('span',class_='price').find_all('span')[-1].text.strip()

        old_price = container.find('div',class_='price-container clearfix')\
            .find('span',class_='price-box').find('span',class_='price -old ').find_all('span')[-1].text.strip()
        # rating = container.find('div',class_='total-ratings').text[1:-1]

        try:
            rating = container.find('div',class_='total-ratings').text[1:-1]
        except:
            rating =0

        my_dict = {}
        my_dict['name']=name
        my_dict['brand']=brand
        my_dict['new_price']=new_price
        my_dict['old_price']=old_price
        my_dict['rating']=rating
        my_dict['image']=image1

        output.append(my_dict)

        # print(image1)
        # print(brand)
        # print(name)
        # print(new_price)
        # print(old_price)
        # print(rating)

        # print()

        #csv_writer.writerow([name,brand,new_price,old_price,rating,image1])



for i in range(25):
    if i!=0:
        base_url = base_url+"&page="+str(i+1)
    
    make_csv(base_url)
        


# make_csv(base_url)

print(len(output))

df = pd.DataFrame(output)

df.to_csv('output.csv', index=False)

# keys = output[0].keys()

# print(keys)

# with open('daraz_scrap.csv', 'wb') as f:
#     w = csv.DictWriter(f, keys)
#     # w.writeheader()
#     w.writerows(output)

# csv_file = open('daraz_scrap.csv','w')
# csv_writer = csv.writer(csv_file)
# csv_writer.writerow(['name','brand','new_price','old_price','rating','image_url'])

# for my_dict in output:
#     csv_writer.writerow([my_dict['name'],my_dict['brand'],my_dict['new_price'],my_dict['old_price'],my_dict['rating'],my_dict['image']])

# # print(container.prettify())
# csv_file.close()







