def string (s):

    if len(s)== 1:
        return s[0]
    else:
        a = s[0]
        return string(s[1:]) + a
    
x = "bat" 

print(string(x))
             