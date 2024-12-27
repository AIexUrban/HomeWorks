def add_everything_up():
    a,b = input('Введите первое значение >>> '),input('Введите второе значение >>> ')
    try:
        if a and b is type(int):
            return int(a + b)
        else:
            return round(float(a)+float(b),3)
    except ValueError:
        return str(a)+str(b)

print(add_everything_up())
