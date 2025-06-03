def keypad (dig):
    l = {"2":"abc","3":"def","4":"ghi","5":"jkl","6":"mno","7":"pqrs","8":"tuv","9":"wxyz"}
    if dig == "":
        return [""]
    leters = l[dig[0]]
    rest = keypad(dig[1:])

    result = []

    for letter in leters:
        for r in rest :
            result.append(letter + r)
    return result 
  
print(keypad("245")) 
    
                    