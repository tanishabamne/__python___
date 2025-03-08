# def sqr (n):
#     return n+5
# l1=eval(input("enter any collection"))
# x=map(sqr,l1)
# print(x)
# print(list(x))


# alag alag l1 mai 1 or 2 wale index ko add krna h
# loop 2 baar chalega
l1=[1,2,3,4,5]
l2=[2,3,4,5]
l3=[3,4]
def add(x,y,z):
    return x+y+z
p=tuple(map(add,l1,l2,l3))
print(p)    