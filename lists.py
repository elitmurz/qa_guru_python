
#Делаем списки!

l=[1, 2, 3, "a", "b", "c",[4, 5, 6]]

print(l[0])

print(l[-1])

print(l[-1][0])

print(l[::-1])

l.append("new element")
l.extend(["elem"])
len(l)

print(l)

l[0] =200
print(l)


#Множества

s = {1, 2, 3, 4, 5, 5, 5, 5, 5,}
s1 = {1, 2, 3, 4, 5, 5, 5, 5, 5,}
s2 = {1, 2, 3, 4, 5, 5, 5, 5, 5,}

print(s)
print(s1)
print(s2)

s.intersection(s2)
s-s1

print(list(set([1, 2,3,4,5,5,5,5,6,7,8,7,6,6,6])))

