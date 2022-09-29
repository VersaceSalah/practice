from datetime import datetime, timedelta

while True:
    try:
        year = int(input('Введите год рождения:\t'))
        month = int(input('Введите месяц рождения:\t'))
        day = int(input('Введите день рождения:\t'))
        birthday = datetime(year, month, day)
        print('\n')
        break
    except ValueError:
        print('\nДанные некоректные\n')
    except TypeError:
        print('\nДанные некоректные\n')

days = timedelta(hours=24 * 10 ** 4, minutes=0, seconds=0)
minutes = timedelta(hours=0, minutes=10 ** 6, seconds=0)
seconds = timedelta(hours=0, minutes=0, seconds=10 ** 9)

print(f'Через {10 ** 4} дней пользователю исполится {birthday + days}')
print(f'Через {10 ** 6} минут пользователю исполнится {birthday + minutes}')
print(f'Через {10 ** 9} секунд пользователю исполнится {birthday + seconds}')
