# Average_Rating

grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

grades_average = [(sum(i) / len(i)) for i in grades] # создаем новый список со средними
# значениями каждого элемента из списка grades

students_list=list(students) # преобразуем множество в список для дальнейшей сортировки
students_list.sort() # Сортируем список по алфавиту
result = dict(zip(students_list , grades_average)) # объединяем два списка в один словарь

print(result)

#END




