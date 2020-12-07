k = int(input('Введите сумму кратную 10: '))

deng = [1000, 500, 200, 100, 50, 20, 10]
rez = []

if k % 10 == 0:
    for i in deng:
        
            if k > 0:
                res = k // i
                k = k - res * i
                # print (res, 'x', i, ', ')
                rez.append(res)

else:
    k = int(input('!!!Error!!!'))   

viv = []

for i in range(len(rez)):
    viv.append(f'{deng[i]}*{rez[i]}')
print (viv)
