A = [64,25,12,22,11]
for i in range(len(A)):
    min_id = i 
    for x in range (i+1,len(A)):
         if  A[min_id] > A[x]:
              min_id = x
    A[i],A[min_id] = A[min_id] , A[i]


print("Sorted Array :")
for i in range(len(A)):
     print(A[i],end = " ")
              

