# a function without name
# use lamdba keyword
# it takes n number of arguments
# but execute  only  single line of expresion

# syntax-----> lamda arrgument: expression 

# x=10
# y=30
# res=lambda p,q:p+q
# print(res(x,y))


# x=10
# y=30
# res=lambda p,q: print(p+q)
# (res(x,y))


# syntax-----> ( lambda+ if else ) ka code neeche hai

x=78
res=lambda y:'even' if(y%2==0) else 'odd'
print(res(x))

# syntax-----> ( lambda+ for loop)
# l1=[]
# for i in range(1,4):
#     l1.append(i)
# l2=[]
# for i in range(4):
#     l2.append(l1)
#     print(l2)

# same code with lambda

# syntax------> lambda  x:[ i for i in collection(string,tuple,list,range)]

# x='tanisha'
# z=lambda x:[p for p in x]
# print(z(x))

# x=4
# res=lambda p:[[i for i in range (1,p) ]for k in range (p)]
# print(res(x))

# for _ in range (4):
#     print('hello')

# lamda with map

# l1=[1,2,3,4]
# def my_sqr(n):
#     return n**2
# x=list(map(my_sqr,l1))
# print(x)

# # with map
# l1=[1,2,3,4]
# x=list(map(lambda x: x**2,l1))
# print(x)

# l1=[1,2,3,4,5]
# x=list(map(lambda x: 'even' if x%2==0 else 'odd',l1))

# lambda with filter for even
# l1=[1,2,3,4]
# x=list(filter(lambda x: x if x%2==0 else None,l1))
# print(x)


# lambda with filter for odd
# l1=[1,2,3,4]
# x=list(filter(lambda x: x if x%2!=0 else None,l1))
# print(x)
# find maximum value


# from functools  import reduce
# l1=[10,2,3,4]
# x=reduce(lambda x,y: x if x>y else y,l1)
# print(x)


x=lambda p:[i for i in range(2,11,2)]
print(x(10))

