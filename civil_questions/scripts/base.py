from bs4 import BeautifulSoup
import requests
from civil_helper import get_question
import json

base_url ='https://www.indiabix.com/civil-engineering'

total_page = 10


data = {}

data['questions'] = []



def load_question(page_number,subject_name):

        url = base_url+"/"+subject_name+"/"+page_number
        try:
                source = requests.get(url).text
                soup = BeautifulSoup(source,'lxml')

                print(page_number)
        except:
                print("Except Called")

    # get All question from Soup

        for container in soup.find_all('div',class_='bix-div-container'):
                question =get_question(container)

                # Appending Question to data list
                data['questions'].append(question)

                #print(question)

def civil_script(subject_name,section_range):

    for i in section_range:
        first_section = "{0:0>3}".format(i)

        for i in range(total_page):
            second_section = "{0:0>3}".format(i+1)

            page_number = first_section+second_section

            load_question(page_number,subject_name)

    with open('../output_data/'+subject_name+'.json', 'w') as outfile:  
        json.dump(data, outfile,indent=4)


# for i in range(23,29,1):
#     first_section = "{0:0>3}".format(i)

#     for i in range(total_page):
#         second_section = "{0:0>3}".format(i+1)

#         page_number = first_section+second_section

#         load_question(page_number,subject_name)



# with open('../output_data/soil_mechanics.json', 'w') as outfile:  
#     json.dump(data, outfile,indent=4)