global a, b, c
def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)

# Task no.1
print('-------------')
print_params()
print_params(2,3)
print_params(b = 'Urban')
print_params(c = 55)
print_params(b= 25)
print_params(c = [1,2,3])
print_params(c = [1,2,3], b = 88)

#Task no.2
print('---------------')
values_list = [4, [1,2,3,4], 'список']
values_dict = {a:2, b:5, c:'Empty'}
print_params(*values_list, **values_dict)
#print_params(**values_dict)

# Task no.3
print('----------------')
values_list_2 = [54.32, 'Строка' ]
print_params(*values_list_2, 42)

# Example - не надо делать вот так: def a(my_list = []))
def append_to_list(item, list_my=None):
    if list_my is None:
        list_my = []
        list_my.append(item)
print(list_my)


append_to_list()



