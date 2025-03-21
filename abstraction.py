# from abc import ABC,abstractmethod
# class A (ABC):
#     def new(self):
#         print("80%")
#         @abstractmethod
#         def new1(self):
#             pass
# class B(A):
#     def first(self):
#         print("20%")
# obj=B()
# obj.new()       

from abc import ABC, abstractmethod
class bank(ABC):
    def registration(self):
        print("registration page")
    def logout(self):
        print("logout-page")
    @abstractmethod
    def authentication(self):
        pass
    def dashboard(self):
        print("from dashboard")
class webapp(bank):
    def login(self,id,pass1):
        self.id=id
        self.pass1=pass1
    def authentication(self):
        print(" authentication ")        
    