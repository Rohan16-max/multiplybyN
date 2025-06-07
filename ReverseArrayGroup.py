def reverse(a,a_size,n):
    tem = 0
    while (tem<a_size):
        start = tem
        end = min(tem + n-1,a_size-1)
        while (start <end):
            a[start],a[end] = a[end] ,a[start]
            start+=1
            end-=1
        tem +=n

a = [5,23,5,2,3,17,18,12]
n = 2
a_size = len(a)
reverse(a,a_size,n)
print(a)