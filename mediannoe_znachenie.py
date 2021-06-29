data = [int(i) for i in input("Введите данные для анализа медианного значения ").split()]
if len(data) > 1:
    data.sort() # сортируем данные
    print (data[int(len(data)/2)]) # выводим среднее значение
elif len(data) == 1:
    print(data[0])
else:  # не ввели данные
    print("Нет данных для анализа")