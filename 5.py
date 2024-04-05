import random
def ygadai():
    a = [random.randint(1, 10) for _ in range(5)]
    b= int(input("Введите число от 1 до 10: "))
    if b < 1 or b > 10:
        print("Проверьте условие! ")
    else:
        if b in a:
            print("Поздравляю, Вы угадали число!")
        else:
            print("Нет такого числа!")
        print("Загаданный список:", a)
def povtor():
    num = [random.randint(1, 10) for _ in range(10)]
    print("Список случайных чисел: ",num)
    a = 10
    res = []
    seen = set()
    for i in range(a):
        if num[i] in seen:
            if num[i] not in res:
                res.append(num[i])
        else:
            seen.add(num[i])
    print("Повторяющиеся числа:", res)
def vixodnoi():
    weekd = ('Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'Воскресенье')
    weekd_d = int(input("Сколько выходных в неделю? "))
    if weekd_d > len(weekd):
        print("Введено слишком много выходных!")
    else:
        weekend = weekd[-weekd_d:]
        workdays = weekd[:-weekd_d]
        print("Ваши выходные дни:", weekend)
        print("Ваши рабочие дни:", workdays)
def play():
    play1 = ('Бабуркин', 'Ковалёв', 'Быков', 'Носов', 'Мамонтов', 'Евсеев', 'Мишин', 'Комиссаров','Устинов','Лихачёв')
    play2 = ('Стрелков', 'Сидоров', 'Рожков', 'Сысоев', 'Русаков', 'Веселов', 'Кулагин', 'Лапин','Исаев','Туров')
    team1 = random.sample(play1, 5)
    team2 = random.sample(play2, 5)
    team_all = tuple(team1[:5] + team2[:5])
    print("Первая группа:", play1)
    print("Вторая группа:", play2)
    print("Спорт команда:", team_all)
    print("Длина кортежа:", len(team_all))
    sorted_team_all = tuple(sorted(team_all))
    print("Отсортированная спорт команда: ", sorted_team_all)
    ivanov = "Иванов"
    if ivanov in team_all:
        print("Иванов есть в команде ", team_all.count("Иванов "))
    else:
        print("Ивановa нет в команде ")
while True:
    print('1.Угадать число')
    print('2. Повторение')
    print('3. Выходные и рабочие дни')
    print('4. Спортивная команда')
    print('5. Выход')
    a = int(input('Выберите действие: '))
    if a == 1:
        ygadai()
    elif a == 2:
        povtor()
    elif a == 3:
        print(vixodnoi())
    elif a == 4:
        print(play())
    elif a == 5:
        break
    else:
        print('Неверное действие')