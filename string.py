
#Строки!

s= "Hello, world"

s= 'Hello, \' "world'

s= """Hello, world"""

s= '''Hello, world'''

s = ' Hello, \n word!' #Символ переноса строки

print(s)

#Cырые строки

s = r"Hello, \\nworld!"
print(s)

#Индексы и слайсы

email = "user@domian.com"

print(email [1])

print (email[0:5])
print (email[0:10:2])

print (email[::-1])

#Оперируем

assert email.endswith("@domian.com")

#Форматируем

a = "Hello"
b = "World"
print("{a}, {b}!".format(a=a,b=b))

print(f"{a}, {b.upper()}!")

print(f" {a=}, {b=}!")  #вывод переменных

print("%s, %s!" %(a,b))

#Строку в число и наоборот

s = "1234"

n =1234

assert s==str(n)
assert int(s)==n



