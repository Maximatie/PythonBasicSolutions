total_salary = 0
for month in range (1, 13):
    print(month, 'месяц')
    salary = int(input("заработная плата: "))
    total_salary += salary
total_salary //= 12
print('средняя зарплата за год равняется', total_salary, 'рублей')
____________________________________________________________________________
danger_count = 0
for sector in range (30, 36):
    print(sector, 'сектор')
    people = int(input('Сколько людей в секторе: '))
    if people >= 10:
        print('Нарушение!')
        danger_count += 1
    elif people < 0:
        print('ошибка !')
    else:
        print('все спокойно!')
print('итого нарушений: ', danger_count)
______________________________________________________________________________

main_number = 0
for i in range(10):
    salary = int(input(''))
    if salary >= main_number:
        print('Упорядочены')
    else:
        print('Не упорядочены')
        break
    main_number = 0
    main_number += salary
________________________________________________________________________________
factorial = 1
number = int(input(''))
for i in range(2, number + 1):
    factorial *= i
print('ответ:', factorial)
________________________________________________________________________________
