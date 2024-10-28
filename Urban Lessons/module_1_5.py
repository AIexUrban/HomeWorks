# Tuples

# item 2
immutable_var = 1,3,8,'Home', False, 'Urban University'
print('Кортеж: ', immutable_var)

# item 3
# Изменяем элементы кортежа:
# immutable_var [1,5] = 'Street', 'Urban' - выходит ошибка
# т.к кортеж является неизменяемым объектом

# item 4
mutable_list= list (immutable_var) # скопировал данные из кортежа и присвоил их списку

mutable_list [1:3] = [5, 'Urban'] # заменяем элементы списка
mutable_list.append('Hello!') # добавили элемент в список
print('Скопированный из кортежа, и измененный список: ', mutable_list)

#END
