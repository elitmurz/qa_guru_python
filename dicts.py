
#Заводим словари

d = {
    "key":"value",
    "another":"another value"
}

user1 = {
    "name": "Vasya",
    "age": 18,
    "id": 25
}

user2 = {
    "name": "Denis",
    "age": 31,
    "id": 13
}

users= {
    25: user1,
    13: user2
}

print(users[13])
print(users[25])

print(user1["name"])
print(user2["name"])

#Функции

users.pop(25)  #Вытаскивает запись из исходнго списка



print("------------------------------------------------")

from pprint import pprint

pprint(list(users.items()))

users.values()

users.keys()

print(users.get(25,{"name": "default user"}))
print(users[13])



