import re
# test = r'用户输入/的字段，正则表达式'
# if re.match(r'段' , test):
#     print('Ture')
# else:
#     print('False')
# print(test)
a = r'a b  c ;, , d'
print(re.split(r'[\s\,\;]+',a))