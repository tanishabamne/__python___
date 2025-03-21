# file---> data ko permanentely store krne ke liye file creat ki jati hai----binary=img,audio----text=string,----csb file=key value pair.
# open---->
# syntax:



# creat first.py
# w mode pe bhi file creat hoti hai
# w mode mai cursor ki position 0 ho jati hai or jis file  mai content likha hota hai vo delete ho jata hai
# a append mai content delete nhi hota file create krta hai  or data override nhi hota hai (best mode hai)

f=open('y1.py','w+')
print(f.mode)
print(f.name)
print(f.readable())
print(f.writable())
print(f.closed)
# operations(CRUD)
# close
