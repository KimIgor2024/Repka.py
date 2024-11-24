import random

A = ("камень", "ножницы", "бумага")
a = random.choice(A)
print("Введите одно из трех: камень, ножницы, бумага: ")
n = str(input())

if a == n:
    print(a)
    print("Ничья")

elif a == "камень" and n == "ножницы":
    print(a)
    print("Ты проиграл!")

elif a == "ножницы" and n == "бумага":
    print(a)
    print("Ты проиграл!")

elif a == "бумага" and n == "камень":
    print(a)
    print("Ты проиграл!")

else:
    print(a)
    print("Ты выйграл")
