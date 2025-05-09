def power1(set1,setsize):
    inner = 0
    outer = 0
    powerset = 2**setsize

    for outer in range (0,powerset):
        for inner in range (0,setsize):
            if(outer &(1<<inner))>0:
                print(set1[inner],end="")
        print()
    
set = [1,2,3]

(power1(set,len(set)))