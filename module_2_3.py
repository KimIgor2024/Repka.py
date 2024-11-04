my_list = [42,69,322,13,0,99,-5, 9, 8, 7, -6, 5]
print(my_list)
i = 0
while  i < len(my_list) :
    print(my_list[i])
    i = i + 1
    number = int(input( " Введите  число  " ))
    if number % 2 == 0:
        print(" число  четное  ")
        continue
    elif number < (0 + (-1)):
        print("Я, за циклом ")
    elif number % 2 != 0 :
        print(" число  нечетное ")

