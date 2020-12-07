summ = int(input('Введите сумму кратную 10: '))

money = [10, 20, 50, 100, 200, 500, 1000]
maxi = 10
i = 0

res = []

if summ % 10 == 0 and summ <= 18800:

    while summ > 0:
        m = money[i]

        while summ % m != 0:
            # if summ > m:
                # break
            summ += money[i-1]
            res[i-1] = res[i-1] - 1


        if summ <= m * maxi:
            res.append(summ // m)
            summ = 0 
        else:
            summ -= m * maxi
            res.append(maxi)
            i += 1
    
else:
    print("""!!!ОШИБКА!!! 
Сумма не может быть выдана!""")

viv = []

for i in range(len(res)):
    viv.append(f'{money[i]} x {res[i]}')

print (viv)

