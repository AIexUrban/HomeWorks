# Average_Rating

grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

students_list=sorted(students) # сортируем множество по алфавиту

result = dict(zip(students_list , ([(sum(i) / len(i)) for i in grades]))) # объединяем
# два списка в один словарь с усредненным значением к каждому ключу

print(result)

#END




