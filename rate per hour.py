hrs = input('Enter Hours')
rate = 10.50
if hrs < 40:
  print(float(hrs) * float(rate))
  if hrs > 40:
    float(rate) * 1.5
    print(float(rate) * hrs)
