def computepay(h, r):
    try:
        h = float(hrs)
        r = float(rate)
    except:
        print("Error!!! Enter numeric input")
        quit()
    if h < 40:
        grosspay = (h * r)
        return(grosspay)
    else:
        grosspay = (h * r)
        extra = ((h -40) * (r * 0.5))
        grosspay = grosspay + extra
        return(grosspay)


hrs = input("Enter Hours: ")
rate = input("Enter Rate: ")
p = computepay(hrs, rate)
print("Pay", p)
