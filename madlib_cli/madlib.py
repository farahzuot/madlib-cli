import re

print('WELCOME! you are going to play madlib with me .. \nI wall ask you for a list of words to substitute for blanks in a story before showing it to you.\nWell, just answer on the command line and press ENTER')

def read_template(path):
    with open(path,'r') as file:
        text = file.read()
        return text



def parse_template():
    content = read_template('assets/madlip.txt')
    extract_text = re.sub(r'\(.+?\)','',content)
    parsed_text = re.sub(r'\{.*?\}','{}',content)
    list_of_words = re.findall('{(.+?)}',extract_text)
    return parsed_text,list_of_words


def merge_template():
    parse_template_function = parse_template()
    updated_text = parse_template_function[0]
    words_list = parse_template_function[1]
    
    new_list=[]
    for i in words_list:
        word_input = input(f'write a {i}: ')
        new_list.append(word_input)
    result=updated_text.format(*tuple(new_list))
    print(result)
    return result



def write_the_result():
    result = merge_template()
    with open('madlib_cli/madlip_final.txt','w') as file:
        text=file.write(result)

    return text

write_the_result()

