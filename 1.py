pattern="";    
for row in range(1,7):    
    for column in range(1,6):     
        if (((column == 1 or column == 5) and row != 1 and row != 6) or ((row == 1 or row == 6) and column > 1 and column < 5)):  
            pattern=pattern+"*"    
        else:      
            pattern=pattern+" "    
    pattern=pattern+"\n"    
print(pattern)