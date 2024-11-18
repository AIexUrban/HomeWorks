import tkinter as tk

window = tk.Tk()
window.title('Калькулятор')
window.geometry('350x350')
window.resizable(False, False)

# from tkinter import *
# root = Tk()
# def hi(i):
#  print(i)
# for i in range(10):
#  Button(text=str(i), command=lambda i=i: hi(i)).pack()
# root.mainloop()

add,sub, mul, div = ["+", "-", '*', '/']
buttons_txt = {add:"+", sub:"-", mul:'*', div:'/'}
i=0
for key, value in buttons_txt.items():
 button = tk.Button(window, text = buttons_txt[value])
 button.place(x=290, y=50+(i*50)+20)
 i += 1
 buttons_txt[value] = i

# label = tk.Label(text="Hello, Tkinter!",
#                  bg="#023946", fg="white",
#                  font=("Arial", 10), height=5, width=40)
# label.pack()
#
# button = tk.Button(text="Нажми на меня!",
#                    font=("Time New Roman", 10), height=1,
#                    width=15, bg="#023946", fg="white",)
# button.pack()


window.mainloop()