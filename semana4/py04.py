lista = [1, 2, 5, 4]

for i in lista:
    print(i)
print('')

for i in range(len(lista)):
    print(i, lista[i])
    print('')

print('-1', lista[-1])
print(":2", lista[:2])
print("2:", lista[2:])

print('Append, insert and extend')
lista.append(6)
print(lista)
lista.insert(2,7)
print(lista)

lista2 = [8,9]
lista.append(lista2)
print(lista)
lista = [1, 2, 5, 4]
lista.extend(lista2)
print(lista)

print("")
print('pop')
lista.pop()
print(lista)
pop = lista.pop()
print(lista, pop)

print("")
print('sort, inversa and index')
lista.sort()
print(lista)
lista.reverse()
print(lista, lista.index(2))

print("")
print('str operations')
lista = ['a', 'b', 'c', 'd']
print(', '.join(lista))
print(', '.join(lista).split(', '))

print("")
print("list1 = list2 ou list1 = list2.copy()")
list1 = [1, 2, 3, 4]
list2 = list1
print(list1, list2)
list1[0] = 0
list1[3] = 5
print(list1, list2)


print("")
list1 = [1, 2, 3, 4]
list2 = list1.copy()
print(list1, list2)
list1[0] = 0
list1[3] = 5
print(list1, list2)

#tuple nao pode ser modificado, so consultado e os elementos de set não são organizados
emptyList = []
emptyList = list()
emptyTuple = ()
emptyTuple = tuple()
emptySet = {}
emptySet = set()