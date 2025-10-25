def inverser_chaine(chaine): 
    stack =[]    
    for i in chaine:
        stack.append(i)
    rev = ''
    while stack :
     rev+= stack.pop()
    
    
    return rev




stack =[] 
print(inverser_chaine("Hello")   )