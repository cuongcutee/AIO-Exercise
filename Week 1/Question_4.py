import math
def factorial(n):
    if n==1:
        return 1
    else:
        return n*factorial(n-1)
def approx_sin(x,n):
    if n == 0:
        return x
    else:
        return approx_sin(x,n-1)+math.pow(-1,n)*math.pow(x,2*n+1)/factorial(2*n+1)
def approx_cos(x,n):
    if n == 0:
        return 1
    else:
        return approx_cos(x,n-1)+math.pow(-1,n)*math.pow(x,2*n)/factorial(2*n)
def approx_sinh(x,n):
    if n==0:
        return x
    else:
        return approx_sinh(x,n-1)+ math.pow(x,2*n+1)/factorial(2*n+1)
def approx_cosh(x,n):
    if n == 0:
        return 1
    else:
        return approx_cosh(x,n-1)+math.pow(x,2*n)/factorial(2*n)

