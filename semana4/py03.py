print('+', 3+2,'; -', 3-2,'; *', 3*2,'; /', 3/2,'; //', 3//2,'; **', 3**2,'; %', 3%2)
message = ""
for i in range(10):
    message += "i = "
    message += str(i)
    message += ': '
    if(i%2==0):
        message += "par ; "
    else:
        message += "impar ; "
print("")
print(message)

num = 3.14159265359
message = ""
for i in range(5):
    message += "i = "
    message += str(i)
    message += ': '
    message += str(round(num, i))
    message += '; '
print("")
print(message)

print('')
print(2>1)