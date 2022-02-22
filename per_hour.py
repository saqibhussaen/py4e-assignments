hrs = input('Enter Hours: ')
rate = input('Enter rate: ')
try:
    h = float(hrs)
    r = float(rate)
except:
    print("Error!!! Enter numeric input")
    quit()
if h < 40:
    grosspay = (h * r)
    print(grosspay)
else:
    grosspay = (h * r)
    extra = ((h -40) * (r * 0.5))
    grosspay = grosspay + extra
    print(grosspay)
