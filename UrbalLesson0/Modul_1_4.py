# Programms organization and strings metods

my_string = input('Введите текст: ')
print('Количество символов в тексте -', len(my_string))

print(my_string.upper()) # строка my_string в верхнем регистре
print(my_string.lower()) # строка my_string в нижнем регистре
print(my_string.replace(' ', '')) # в строке my_string удаляем все пробелы.
print(my_string[0])
print(my_string[-1])

# END

# print(my_string.capitalize()) # Первая буква заглавная
# print(f'{my_string[:-1]}{my_string[-1].upper()}') # Последняя буква заглавная
