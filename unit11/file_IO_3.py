f = open('unit11/file3.txt', 'w')
lines = ['line 1\n', 'line 2\n', 'line 3\n']
f.writelines(lines)
f.close()


f = open('unit11/file3.txt')
# print(f.readline())  #for reading only one line
# print(f.readlines())  #for reading all lines 


while True:   #for reading all lines
    line = f.readline()
    if not line:
        break
    print(line)
