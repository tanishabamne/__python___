# class student:
#     school='shsss' #static variable
#     city='bhopal'  #static variable
#     def__init__(self,name,rol):
#            self.x=name
#     selfy=rol
# _____________________________________________________________
class student:
    school='shss'        #static variable
    def __init__(self,name,roll):
           self.x=name  
           self.y=roll
           student.city='bhopal'  #static
    def show(self):
         student.s_code=123
    def display(self):
         print(student.s_code)
         print(student.city)
         print(student.school)
         print(student.principal)
student.principal='rahul'  #static
obj=student("tanisha",101)
obj.show()
obj.display()
print(student.school)  


