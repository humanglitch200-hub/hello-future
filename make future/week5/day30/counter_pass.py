with open('lines.txt', 'r', encoding = 'utf-8') as f:
    count = 0
    acount = 0
    for l in f:
        count += 1
        if 'a' in l:
            acount += 1           
    print("Total lines that contains a: ", acount)
    print("Total lines: ", count) 
    
        

            