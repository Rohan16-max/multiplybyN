input_num = int(input("Enter any number:-"))

origin = input_num
reverse = 0

while input_num>0 :
    digit =input_num % 10 
    reverse = reverse * 10 + digit
    input_num  //= 10

if origin == reverse:
    print(f"{origin}\nIts is a Palindrome Number. ")

else:
    print(f"{origin}\nIts is not a Palindrome Number. ")