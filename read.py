iput = input("File address")
print("Reading= ", iput)
with open("iput", "r") as file1:
    file_stuff=file1.read()
    print(file_stuff)
print(file1.closed)
print(file_stuff)