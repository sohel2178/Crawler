from bs4 import BeautifulSoup
import requests
import pandas as pd

base_url ='https://bikroy.com/en/ads/dhaka/electronics'

source = requests.get(base_url).text
soup = BeautifulSoup(source,'lxml')

output =[]

for item in soup.find_all('div',class_='ui-item'):
    item_thumb = item.find('div',class_='item-thumb')

    try:
        image = (item_thumb.a.img['data-srcset'].split(',')[0]).split(' ')[0]
    except:
        image = None
    
    if image != None:
        image = "https:"+image


    item_content = item.find('div',class_='item-content')

    name = item_content.a.text.encode("ascii","ignore").decode('utf-8')
    location = item_content.p.find('span',class_='item-area').text
    category = item_content.p.find('span',class_='item-cat').text

    my_dict={}
    my_dict['name']=name
    my_dict['location']=location
    my_dict['category']=category
    my_dict['image']=image

    output.append(my_dict)


    # print(image)
    # print(name)
    # print(location)
    # print(category)

    # print()

print(len(output))

df = pd.DataFrame(output)

df.to_csv('bikroy.csv', index=False)



# print(item_content.prettify())