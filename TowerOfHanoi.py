def tower_of_hanoi(n,s,a,d):

    if n == 1:
        print("move disk 1 from",s,d,a)

        return
    tower_of_hanoi(n-1,s,d,a)
    print("move disk from",s,d)
    tower_of_hanoi(n-1,a,s,d)

tower_of_hanoi(3,'A','B','C')   