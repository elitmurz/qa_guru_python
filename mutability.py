
#Списки, словари и множества -изменяемые!

from copy import deepcopy

l1 = [1, 2, 3,[5,6,7]]
#l2=l1.copy()

l2 = deepcopy(l1)
l2[-1].append(8)
l2.append()

print(l2)

l2.append(4)  #Добавление 4 во второй список

print(l2)
print(l1)

#Кортежи

t  = (1,2,3,4,5,6)

t[1:3]

print(t)

t.count(1)
print(t)


f = frozenset({1,2,3,4,5,6,7,8})

print(f)