str="tanisha"
vol=con=0
i=0

while i<len(str):

   x=('a','e','i','o','u','A','E','I','O','U')
   y=str[i]
    
   if y in x:
    vol=vol+1
   else:
    con=con+1
i=i+1
print(vol)
print(con)