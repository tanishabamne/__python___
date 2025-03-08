# method---->instance method ,  class method ,static method

# instance ----> pehla parameter self use hota hai
# class student:
#     def first(self):
#         print("This is from first")
#     def second(self):
#         student.first(self)
# obj=student()
# obj.first()
# obj.second()

#  class method----> @classdecorator and  @classmethod same hai @--->decorator
# static variable and object variable ko call kerne ke liye class method ko use krte hai

# class book:
#     price =100             
#     total_pages=500
#     def __init__(self,stu_name):
#         self.x =stu_name
#         print(self.x,book.price,book.total.pages)
#     @classmethod
#     def update(cls,p,q):
#          cls.price=p
#          cls.total.pages=q
# book.update(150,600)
# obj4=book('vishnu')
# obj5=book('arvind')         

# static method ---------->@staticmethod

# class book:
#     def __init__ (self):
#       print("constructor called")
# @staticmethod
# def welcome():
#     print("welcome to my page")
# @staticmethod
# def thanks():
#     print("thanks for visit")
#     # obj.book()
#     book.welcome()  


class book:
    def __init__(self):
        print("constructor called")
    @classmethod
    def welcome(cls,name):
        cls.x=name
    def show(self):
        print(book.x)
obj=book()
book.welcome('tanisha')
obj.show()
print(book.x)



