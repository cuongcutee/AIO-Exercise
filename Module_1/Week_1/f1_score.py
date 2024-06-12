import math

def exercise1(tp,fp,fn):
    if type(tp) != int:
        print("tp must be int")
        return
    if type(fp) != int:
        print("fp must be int")
        return
    if type(fn) != int:
        print("fn must be int")
        return
    if tp < 0 or fp < 0 or fn < 0:
        print("tp and fp and fn must be greater than zero")
        return
    precision = tp/(tp+fn)
    recall = tp/(tp+fp)
    f1_score = 2*((precision*recall)/(precision+recall))
    return f1_score


