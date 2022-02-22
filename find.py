text = "X-DSPAM-Confidence:    0.8475"
st = text.find('0')
ed = text.find('5')
host = text[st:ed+1]

print(float(host))