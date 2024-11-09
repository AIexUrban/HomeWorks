def count_calls(): # Функция - счетчик вызовов
    global calls
    calls += 1
    return calls


def string_info(string):
    count_calls() # Вызываем функцию "счетчик вызовов"
    result_tuple = (len(string), string.upper(), string.lower())  # Выполняем условие №2 задания
    return result_tuple  # Функция возвращает кортеж согласно задания №2


def is_contains(string: str, list_to_search: list):
    count_calls()  # Вызываем функцию "счетчик вызовов"
    string = string.upper()  # Перевод строки в верхний регистр
    joined_string = " ".join(list_to_search)  # Переводим список в строку для дальнейшей смены регистра
    joined_string = joined_string.upper()  # Переводим строку в в ерхний регистр
    if string in joined_string:  # Определяем, есть ли строка в первоначальном списке
        return True
    else: return False

calls = 0
print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches
print(calls)

#END
