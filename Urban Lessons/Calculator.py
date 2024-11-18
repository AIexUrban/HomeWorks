import tkinter as tk


def get_values():
    num1 = int(number1_entry.get())
    num2 = int(number2_entry.get())
    return num1, num2


def insert_values(value):
    answer_entry.delete(0, 'end')
    answer_entry.insert(0, value)


def add():
    num1, num2 = get_values()
    res = num1 + num2
    insert_values(res)


def sub():
    num1, num2 = get_values()
    res = num1 - num2
    insert_values(res)


def div():
    num1, num2 = get_values()
    res = num1 / num2
    insert_values(res)


def mul():
    num1, num2 = get_values()
    res = num1 * num2
    insert_values(res)


window = tk.Tk()
window.title('Калькулятор')
window.geometry("350x350")
window['bg'] = '#023946'
window.resizable(False, False)
button_add = tk.Button(window, text="+", width=2, height=2, bg="#027936", fg="white", command=add)
button_add.place(x=300, y=50)
button_sub = tk.Button(window, text="-", width=2, height=2, bg="#027956", fg="white", command=sub)
button_sub.place(x=300, y=100)
button_mul = tk.Button(window, text="*", width=2, height=2, bg="#027976", fg="white", command=mul)
button_mul.place(x=300, y=150)
button_div = tk.Button(window, text="/", width=2, height=2, bg="#027996", fg="white", command=div)
button_div.place(x=300, y=200)
number1_entry = tk.Entry(window, width=28)
number1_entry.place(x=100, y=75)
number2_entry = tk.Entry(window, width=28)
number2_entry.place(x=100, y=150)
answer_entry = tk.Entry(window, width=28)
answer_entry.place(x=100, y=300)
number1 = tk.Label(window, text="Введите первое число:", bg="#023946", fg="white")
number1.place(x=100, y=50)
number2 = tk.Label(window, text="Введите второе число:", bg="#023946", fg="white")
number2.place(x=100, y=125)
answer = tk.Label(window, text="Ответ:", bg="#023946", fg="white")
answer.place(x=100, y=275)
window.mainloop()