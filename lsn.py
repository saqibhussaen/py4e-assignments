lar = 0
sm = None
while True:
    num = input("Enter a number: ")
    if num == 'done':
        break
    try:
        ival = int(num)
    except:
        print("Invalid input")
        continue
    if ival > lar:
        lar = ival
    if sm is None:
        sm = ival
    elif ival < sm :
        sm = ival
print("Maximum is", lar)
print("Minimum is", sm)
