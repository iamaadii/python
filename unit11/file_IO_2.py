with open('unit11/file2.txt', 'r') as f:
    print(f.read())
with open('unit11/file2.txt', 'w') as f:
    f.write("how are u")
with open('unit11/file2.txt', 'a') as f:
    f.write("\ni am fine")
with open('unit11/file2.txt', 'r') as f:
    print(f.read())