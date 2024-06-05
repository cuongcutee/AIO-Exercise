import math
def is_number(n):
    try:
        float(n)
    except ValueError:
        return False
    return True

def exercise2():
    anpha = 0.01
    x = input("x = ")
    if is_number(x) == False:
        print("x must be a number")
        return
    activation_function = input("activation_function = ")
    if activation_function != "sigmoid" and activation_function != "relu" and activation_function != "elu":
        print(f"{activation_function} is not supported")
        return
    if activation_function == "sigmoid":
        return 1/(1+math.exp(-float(x)))
    if activation_function == "relu":
        return max(0,float(x))
    if activation_function == "elu":
        if float(x) < 0:
            return (math.exp(float(x)) - 1) * anpha
        else:
            return float(x)


      