greeting='Hello world!'

count_o = 0

for i in greeting:
    if i == 'o':
        count_o += 1
        print(i)

print(count_o)

students = ['Вася','Петя', 'Николай', 'Александр']

for student in students: # Цикл в цикле
    print(student)
    for char in student:
        print(char)





