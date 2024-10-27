# Strings & Indexes

example = 'Топинамбур'
print(len(example))

print(example[0]) # первый символ этой строки
print(example[-1]) # последний символ этой строки (используя отрицательный индекс)

i=len(example) # Вывод второй половины строки
a=i//2
if len(example[a:])%2==0: # проверка на нечетность кол-ва букв
    print(example[a+1:])  # при выводе второй половины строки
else:
    print(example[a:])


print(example[::-1]) # это слово наоборот
print(example[1::2]) # каждый второй символ этой строки

#END
