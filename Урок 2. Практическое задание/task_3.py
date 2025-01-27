"""
3. Пользователь вводит месяц в виде целого числа от 1 до 12.
Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
Напишите два варианта решения: через list и через dict.

Пример:
Введите номер месяца: 10
Результат через список: Осень
Результат через словарь: Осень
"""

seasons_list = ['зима', 'весна', 'лето', 'осень']
seasons_dict = {1: 'зима', 2: 'весна', 3: 'лето', 4: 'осень'}
month = int(input("Введите номер месяца: "))
season = 0

if month > 12 or month < 1:
    print("Неправильный ввод")
else:
    if month < 3 or month == 12:
        season = 1
    elif month < 6:
        season = 2
    elif month < 9:
        season = 3
    else:
        season = 4

    print(f"Результат через список: {seasons_list[season - 1]}")
    print(f"Результат через словарь: {seasons_dict.get(season)}")
