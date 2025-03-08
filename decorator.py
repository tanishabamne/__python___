# kisi bhi function ke code ko change kiye hue uske internal behaviour ko change krne k liye Decorator use kerte hai

# special type ka heigher order function hai ye--
#  as  a argument ek function leta hai orr ek function hi return krta hai


# ___________________1st example
# def outer_fun(new):
#     def inner_fun():
#         print("hello")
#     return inner_fun
# @outer_fun
# def new():
#     pass
# new()    
 
def outer_fun(s):
    def inner_fun(p,q):
        p=p+10
        q=q+10
        r=s(p,q)
        print(r)
    return inner_fun
@outer_fun
def new(x,y):
    return x+y
p=10
q=20
new(p,q)