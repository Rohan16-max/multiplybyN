def num (num1,num2):

    if (num1 ^ num2 !=0 ):
        print("The numbers are not equal.")

    else:
        print("The numbers are equal.")

user = int(input("Enter the first to compare:-"))
user2 = int(input("Enter the second to compare:-"))

num(user,user2)