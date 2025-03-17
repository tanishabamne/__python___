# wrapping variables as well as method in a single unit is called encapsulation.
# eg.------->class
class book:
    price=100
    def __init__(self,name):
      self.author=name
    def add(self,total_pages):
       self.pages=total_pages
    @classmethod
    def update_price(cls,x):
       p="hello"
       cls.price=x
    @staticmethod
    def great():
       print("welcome to my web page") 