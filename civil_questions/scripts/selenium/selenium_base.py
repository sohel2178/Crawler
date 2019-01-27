from selenium import webdriver

import json

import time

base_url = 'http://www.indiabix.com/civil-engineering'

browser = webdriver.Chrome(r'C:\Users\sohel\ChromeDriver\chromedriver.exe')
# browser = webdriver.Firefox()

total_page = 10

data = {}

data['answers'] = []



def print_answer_per_page(page_number,subject_name):

    url = base_url+"/"+subject_name+"/"+page_number

    browser.get(url)
    time.sleep(3)

    answers =browser.find_elements_by_class_name('answer')

    print(len(answers))

    for answer in answers:
        answer.click()
        time.sleep(1)

    actual_answers = browser.find_elements_by_class_name("jq-hdnakqb")


    for answer in actual_answers:
        while answer.text=='':
            continue
        data['answers'].append(answer.text)



def get_all_answer_of_a_section(subject_name,section_range):
    for i in section_range:
        first_section = "{0:0>3}".format(i)

        for i in range(total_page):
            second_section = "{0:0>3}".format(i+1)
            page_number = first_section+second_section

            print(page_number)
            print_answer_per_page(page_number,subject_name)

            # time.sleep(20)

    browser.close()

    with open('../../output_data/'+subject_name+'-answers.json', 'w') as outfile:  
        json.dump(data, outfile,indent=4)





# get_all_answer_of_a_section(section_range)

# browser.close()

# print(len(answer_list))
# print(answer_list)


# //*[@id="divAnswer_101"]/p[1]/span[2]

# //*[@id="divAnswer_164"]/p[1]/span[2]

    # value = browser.find_element_by_xpath('//*[@id="divAnswer_101"]/p[1]/span[2]').text

    # print(value)

