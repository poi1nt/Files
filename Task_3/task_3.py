import os

file_texts = os.walk('texts')
for file_text in file_texts:
    files_name = file_text[2]

dict_file = {}

for name in files_name:
    with open('texts/' + name, 'rt', encoding='utf-8') as file:
        list_text = file.readlines()
        dict_f = {name: list_text}
        dict_file[len(list_text)] = dict_f

sorted_dict_file = dict(sorted(dict_file.items()))

with open('new_file', 'wt', encoding='utf-8') as new_file:
    for len_list, value_dict in sorted_dict_file.items():
        for name_file, text_file in value_dict.items():
            new_file.write(f'{name_file}\n{len_list}\n{"".join(text_file)}\n')