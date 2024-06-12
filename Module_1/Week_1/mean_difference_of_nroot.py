import math
def md_nre_single_sample(y,y_hat,n,p):
    return math.pow(math.pow(y,1/n)-math.pow(y_hat,1/n),p)
