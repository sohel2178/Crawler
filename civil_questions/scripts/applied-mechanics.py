
from base import civil_script

subject_name = "applied-mechanics"

sections = range(23,48,1)


civil_script(subject_name,sections)

# def civil_script(subject_name,section_range):

#     for i in section_range:
#         first_section = "{0:0>3}".format(i)

#         for i in range(total_page):
#             second_section = "{0:0>3}".format(i+1)

#             page_number = first_section+second_section

#             load_question(page_number,subject_name)

#     with open('../output_data/'subject_name+'.json', 'w') as outfile:  
#         json.dump(data, outfile,indent=4)