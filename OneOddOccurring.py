def occur(num):

    r = 0

    for i in num:
        r = r ^ i

    print("the odd number is this",r)

num = [2,3,4,3,2,4,9]

occur(num)