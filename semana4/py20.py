

try:
    f = open('testfile.txt')
except FileNotFoundError as e :
    print('Sorry, This file does not exist')
    print(e)
except Exception as e:
    print(e)
else:
    print(f.read())
    f.close()
finally:
    print("executing Finally...")