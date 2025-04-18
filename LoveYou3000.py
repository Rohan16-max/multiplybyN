smaller = int(input ("Enter a any small number:-"))
bigger = int(input ("Enter a any bigger number:-"))

for i in range(smaller,bigger+1):
        for j in range(2,i):
            if i%j==0:
             break
        else:
           print(i)