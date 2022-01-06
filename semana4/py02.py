message = 'Hello World'

for i in range(len(message)):
    print('message(i) =', message[i])
    print('i= ', i)
    print("");

    
message = message.replace('World', "Universe")
print(message)
print("")

greeting = 'Hello'
name = 'Michael'
message = '{}, {}. Welcome!'.format(greeting, name)
print(message)
print("")


message = f'{greeting}, {name.upper()}. Welcome!'
print(message)
print("")

print(dir(name))