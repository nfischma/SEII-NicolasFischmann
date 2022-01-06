f = open('demo.txt', 'r')
print(f.mode)
print(f.name)
f.close()

print(f.name)
print(f.mode)


with open('demo.txt', 'r') as f:
    print(f.mode)
    print(f.name)
    f_contents = f.readline()
    print(f_contents)
    
    f_contents = f.readline()
    print(f_contents, end = '')
    f_contents = f.readline()
    print(f_contents, end = '')


print('')
print('')   


with open('demo.txt', 'r') as f:
    for line in f:
        print(line, end='')

with open('demo2.txt', 'w') as f:
    f.write('Test')
    f.seek(0)
    f.write('R')

with open('demo.txt', 'r') as rf:
    with open('demo3.txt', 'w') as wf:
        for line in rf:
            wf.write(line)
            