def x (a,b):
   a = a^b 
   b = a^b 
   a = a^b

   print("a is ",a,"and b is",b)

x(12,6)



def Y (a,b):
   a = (a & b) + (a | b)
   b = a +(~b) + 1
   a = a +(~b) + 1

   print("a is ",a,"and b is",b)

Y(2,4)