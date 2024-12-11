f = open('unit11/file3.txt', 'w')
lines = ['line 1\n', 'line 2\n', 'line 3\n']
f.writelines(lines)
f.close()


f = open('unit11/file3.txt')
print(f.readline())
