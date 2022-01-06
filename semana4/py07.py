nums = [1, 2, 3, 4, 5, 6]


for num in nums:
    print(num)
    if num==3:
        break
    elif num == 2: 
        continue
    print('reloop')

x = 0
while x < 10: # ou True
    if x==5:
        break
    print(x)
    x +=1
