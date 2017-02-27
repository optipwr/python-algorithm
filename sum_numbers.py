with open('numbers.txt') as file:
    file_contents_as_list = file.readlines();
    # print file_contents_as_list;

# results = map(int, file_contents_as_list);
# print results;

# stripped_content = ''.join(line.lstrip(' \t') for line in file_contents_as_list.splitlines(True));
# print stripped_content;

# for i in file_contents_as_list:
#     j = i.replace(' ', '')
#     k.append(j)
#     print k;

import re

with open('numbers.txt') as file:
   file_contents_as_list = file.readlines()
   # print file_contents_as_list;
   newString = str(file_contents_as_list)
   result = re.sub('[^0-9]','', newString)
   newList = map(int, result);
   total = sum(newList);
   print total;
