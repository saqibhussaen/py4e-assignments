# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
result = 0
count = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    f0 = line.find('0')
    count = count + 1
    num0 = line[f0:]
    num1 = float(num0)
    result = result + num1
print("Average spam confidence:", float(result / count))