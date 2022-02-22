handle = open('/users/saqib/desktop/mbox.txt').read()
for line in handle:
    if not line.startswith('From: '):
        continue
    parts = line.split()
    email = parts[1]
    print(email)






