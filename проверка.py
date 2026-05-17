import os


files = ['1.txt', '2.txt', '3.txt']


file_contents = []
for file_name in files:
    with open(file_name, 'r', encoding='utf-8') as file:
        content = file.readlines()
        file_contents.append((file_name, len(content), content))


file_contents.sort(key=lambda x: x[1])


with open('result.txt', 'w', encoding='utf-8') as result_file:
    for file_name, line_count, content in file_contents:

        result_file.write(file_name + '\n')
        result_file.write(str(line_count) + '\n')


        result_file.writelines(content)
        result_file.write('\n')