# f = open('D:/tests/FB.txt', 'r')
f = open('FB.txt', 'r')
r = open('result.txt', 'w')


for line in f:

    el = line.split()
    # print ('Считанные числа:', el)
    r.writelines(f'Initial data: {el} \n')
    fi, s, c = el

    fir = int(fi)
    sec = int(s)
    col = int(c)

    res = []

    for i in range(1, col+1):
        
        if ((i % fir == 0) and (i % sec == 0)):
            res.append ('FB')
        elif (i % fir == 0):
            res.append ('F')   
        elif (i % sec == 0):
            res.append ('B')
        else:
            res.append (str(i))

    r.writelines(' '.join(res))
    r.write('\n<============>\n')    
    
    

f.close()
r.close()