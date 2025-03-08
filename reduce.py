from functools import reduce
l1=[1,2,3,4,5,6,7,8]
def mymax(x,y):
    if x>=y:
        return x
    else:
        return y
p=reduce(mymax,l1)
print(p)   