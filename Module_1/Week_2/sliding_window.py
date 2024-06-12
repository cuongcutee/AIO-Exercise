import math

def sliding_window(num_list,k):
    output=[]
    for i in range(len(num_list)-k+1):
        output.append(max(num_list[0+i:k+i]))
    return output

print(sliding_window([3,4,5,1,-44,5,10,12,33,1],3))