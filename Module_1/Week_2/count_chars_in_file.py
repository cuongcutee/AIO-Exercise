import math
def count_chars(string):
    my_dict={}
    for i in range(len(string)):
        if string[i] in my_dict:
            my_dict[string[i]]+=1
        else:
            my_dict[string[i]]=1
    return my_dict

def count_chars_in_file(file_path):
    file = open(file_path,"r")
    data = file.read()
    my_dict=count_chars(data)
    file.close()
    return my_dict
