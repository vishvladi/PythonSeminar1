# Задание 1. Язык математики
# В первый же день на сайте отвалилась формула по расчёту рекламной
# метрики, и только Вася может её поправить. Часть программы с вводными
# данными представлена ниже, отдельно записана формула на математическом
# языке.
# Дана программа:
# a =8
# b =10
# c = 12
# d =18
# Продолжите программу: переведите выражение с математического языка на
# язык Python, запишите его в переменную res и выведите результат.
# Выражение:((-3+2**2)*b-2**3)//c-2*d
#Решение:
#Инициализация переменных с заданными значениями
a=8
b=10
c=12
d=18
#Вычисление числителя формулы:1)Сначала 2 возведим в квадрат.2)Затем прибавляем-3
#3)Умножаем результат на b.4)Вычисляем 2 в степени 3 и вычитаем его из предыдущего результата
dividend=((-3+a**2)*b-2**3)
#Вычисление знаменателя формулы:1)Умножаем 2 на d.2)Вычисляем разность c и полученного результата
divider=(c-2*d)
#Вычисление результата деления числителя на знаменатель
res=dividend/divider
#Вывод результата на экран
print(res)
