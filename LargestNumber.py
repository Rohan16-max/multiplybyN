digits = [8,6,5,8,9,1,3,4]
digits.sort(reverse = True)
largest_number = int("".join(map(str,digits)))

print("Largest number formed :",largest_number)