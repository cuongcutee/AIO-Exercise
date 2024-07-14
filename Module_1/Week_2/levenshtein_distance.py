import numpy as np

def sub_cost(string_1,string_2,i,j):
    if string_1[i]==string_2[j]:
        return 0
    else:
         return 1

def levenshtein_distance(string_1,string_2):
    matrix = np.zeros((len(string_1)+1,len(string_2)+1))
   
    for i in range(len(string_1)+1):
        matrix[i,0]=i
   
    for i in range(len(string_2)+1):
        matrix[0,i]=i
    for i in range(1,len(string_1)+1):
        for j in range(1,len(string_2)+1):
                a = matrix[i-1,j]+1
                b = matrix[i,j-1]+1
                c = matrix[i-1,j-1]+ sub_cost(string_1,string_2,i-1,j-1)                       
                matrix[i,j]=min(a,b,c)
    return int(matrix[len(string_1),len(string_2)])
print(levenshtein_distance('elmets','elements'))

