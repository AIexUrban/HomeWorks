# Вызов разом

def apply_all_func(int_list, *functions):
    result = {}
    int_list = list(map(int, int_list))
    for func in functions:
        result[func.__name__] = func(int_list)
    return  result

print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))
print(apply_all_func([6, 20, '15', '9', '23'], len, sum, sorted))
print(apply_all_func([6.45, 20.3, 15, 9], len, sum, sorted))

# END

