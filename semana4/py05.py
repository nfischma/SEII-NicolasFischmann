conditions = [False, None, 0, 1, 10, True]

for condition in conditions:
    print('condition =', str(condition))
    if condition:
        print('evalutaion : True')
    else:
        print('evaluation : False')
    print("")