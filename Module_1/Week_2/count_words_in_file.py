import math

def count_words_in_file(file_path):
    file = open(file_path,"r")
    data = file.read()
    word=data.split()
    my_dict={}
    for i in word:
        if i in my_dict:
            my_dict[i]+=1
        else:
            my_dict[i]=1
    file.close()
    return my_dict