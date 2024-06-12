import math

def count_chars(string):
    my_dict={}
    for i in range(len(string)):
        if string[i] in my_dict:
            my_dict[string[i]]+=1
        else:
            my_dict[string[i]]=1
    return my_dict
print(count_chars("Happiness"))