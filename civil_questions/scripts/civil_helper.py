

def get_question(container):
    question_json = {}

    question = container.find('td',class_='bix-td-qtxt').find('p').text
    question_json['question'] = question

    question_json['answers'] = []

    answer_main_container = container.find('td',class_='bix-td-miscell')

    for answer_container in answer_main_container.find_all('td',class_='bix-td-option'):

        if answer_container['width'] == '99%':
            question_json['answers'].append(answer_container.text)

    return question_json



