list = ["5", "20" ,"30"]

with open('./filename.txt', mode='wt', encoding='utf-8') as myfile:
    myfile.write('\n'.join(list))
