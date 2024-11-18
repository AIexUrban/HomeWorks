
data_structure = [
[1, 2, 3],
{'a': 4, 'b': 5},
(6, {'cube': 7, 'drum': 8}),
"Hello",
((), [{(2, 'Urban', ('Urban2', 35))}])
]

# Объявляем функцию
def calculate_structure_sum(data):
    summ=0  # Объявляем переменную для подсчета суммы всех эл-ов
    if isinstance(data, (list, tuple, set)):  # Проверяем данные на наличие в ней либо списка или кортежа, или множества
        for i in data:  # Если "ДА" перебираем в итерации очередные данные и\
            summ += calculate_structure_sum(i)  # складываем ("+") значения в итоговую переменныю
    elif isinstance(data, dict):  # Проверяем данные на наличие в ней словарей
        for key, value in data.items():  # Если "ДА", прибавляем к итоговой переменной значение ключей и\
            summ += calculate_structure_sum(key) + calculate_structure_sum(value)  # сами значения, предварительно\
            # переводя словарь в список парных эл-ов и в итерации данной функции складываем их также попарно
    elif isinstance(data, str):  # Если елемент является строкой, то возвращаем\
        return len(data)  # длину этой строки ( summ += len(data)
    elif isinstance(data, int) or isinstance(data, float):  # Если елемент является числим или дробным числом, то возвращаем\
        return data  #  это значение (summ += data)
    return summ


result = calculate_structure_sum(data_structure)
print(result)

# END