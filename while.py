inn = input("Count numbers")
try:
    n = int(inn)
except:
    print("Non Numeric value")
    quit()
num = -1
while n > num:
    num = num + 1
    print(num)
    if num == n:
        break
