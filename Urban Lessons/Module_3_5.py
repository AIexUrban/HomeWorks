# Рекурсивное умножение цифр
def get_multiplied_digits(number):
    number = int(number)  # т.к первоначально переменная в строковом формате, переводим ее в число\
    # для избавления от '0', если число начинается с ноля или нолей перед первой цифрой, отличной\
    # от ноля
    str_number = str(number)  # переводим переменную обратно в строчный режим, но уже без нолей впереди\
    # для дальнейшей работы с ней
    first = int(str_number[0])  # берем первую цифру из заданного числа
    while str_number.endswith('0'): # цикл убирает ноли с конца числа до тех пор, пока не встретит\
        # число, отличное от ноля. Можно было бы, при наличии ноля с конца числа, сразу возвращать\
        # "ноль" и выходить из функции не начиная рекурсию, но задача несколько иная
        str_number = str_number[:len(str_number)-1]  # уменьшаем длину преобразованной переменной на\
        # один ноль сзади, при его наличии, и возвращаемся к началу этого цикла проверки
    if len(str_number) > 1:  # если полученная переменная длиннее одной цифры
        return first * get_multiplied_digits(int(str_number[1:]))  # перемножаем рекурсивно все последующие\
        # цифры после первой
    elif len(str_number) <= 1: # иначе выводим первую и единственную цифру
        return first


result = get_multiplied_digits(str('00004020300000'))  # Для работы данного варианта кода задания, требуется\
  # ввод первоначального числа в текстовом формате (формат строки), т.к невозможно передать в функцию\
  # число, начинающееся с ноля или нолей (указание в Примечании к заданию).
print(result)

# END