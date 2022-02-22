lar = 0
sm = 0.0
while True :
    st = input ('Enter a number: ')
    if st == 'done':
        break
    try:
        ft = int(st)
    except:
        print("Invalid input")
        continue
    print(ft)
    num = num + 1
    tot = tot + ft

print('All Done')
print(tot,num,tot/num)
