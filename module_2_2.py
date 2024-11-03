first = input( "Введите число First:" )
second = input("Введите число Sekond:" )
third = input( "Введите число Third:")
print(first == second == third)
if first == second == third:
    print("если все числа равны , равно 3")
elif first  == second  or first == third or third == second:
    print("если два числа равны ,равно 2")
elif first != second != third:
    print(" если числа не равны ,равно 0 " )