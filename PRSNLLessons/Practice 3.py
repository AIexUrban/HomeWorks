# Определение что вводится - число или строка (метод .isdigit)

integer = input('Enter a number: ')
if integer.isdigit():
    integer = int(integer)
    print("You are entered: ",integer)
    print (type(integer))
else:
    print(f"{integer}, is not number. Pls enter a number")



# END