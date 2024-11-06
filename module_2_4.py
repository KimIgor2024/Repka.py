numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

numbers = int(input("Введите диапазон для поиска простых чисел: "))
for num in range(1, numbers):
    count = 0
    delitel = 2
    while delitel < num:
        if num % delitel == 0:
            count += 1
        delitel += 1
    if count == 0:
        print (f'{num} простое число')

 #   Primes = [1, 2, 3, 5, 7, 11, 13]
 #  Not_primes = [4, 6, 8, 9, 10, 12, 14, 15]