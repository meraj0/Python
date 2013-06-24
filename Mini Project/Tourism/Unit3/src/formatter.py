w= open('input.txt','a')
f=open('format.txt','r')
for line in f:
    line.replace(' ', '')
    if line=='\n':
        newline = line.replace('\n', '')
        w.write(newline)
    else:
        w.write(line)
f.close()
w.close()
