from bs4 import BeautifulSoup
import requests

from civil_helper import get_question

import json


base_url ='https://www.indiabix.com/civil-engineering/surveying'

section = 8
total_page =10


data = {}

data['questions'] = []


def load_question(page_number):
    url = base_url+"/"+page_number
    source = requests.get(url).text
    soup = BeautifulSoup(source,'lxml')

    # get All question from Soup

    for container in soup.find_all('div',class_='bix-div-container'):
        question =get_question(container)

        # Appending Question to data list
        data['questions'].append(question)

        print(question)


for sec in range(section):
    first_section = "{0:0>3}".format(sec+1)

    for page in range(total_page):
        second_sec = "{0:0>3}".format(page+1)

        page_number = first_section+second_sec

        load_question(page_number)

        







# for i in range(total_page):
#     url_arr=[]
#     if i== 0:
#         load_question('')

#     else:
#         load_question("{0:0>3}".format('001')+"{0:0>3}".format(i+1))

with open('../output_data/surveying.json', 'w') as outfile:  
    json.dump(data, outfile,indent=4)




    







# for container in soup.find_all('div',class_='bix-div-container'):

#     question_json = {}

#     question = container.find('td',class_='bix-td-qtxt').find('p').text

#     question_json['question'] = question
#     question_json['answers'] = []


#     answer_main_container = container.find('td',class_='bix-td-miscell')

#     for answer_container in answer_main_container.find_all('td',class_='bix-td-option'):

#         if answer_container['width'] == '99%':
#             question_json['answers'].append(answer_container.text)

    
#     data['questions'].append(question_json)


# with open('civil.json', 'w') as outfile:  
#     json.dump(data, outfile,indent=4)

    


# print(soup.prettify())
