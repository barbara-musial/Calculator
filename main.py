import tkinter as tk


def click(number):
    e.insert(9-0, number)


def add():
    global first
    global action
    action = 'addition'
    first = e.get()
    e.delete(0, 'end')


def sub():
    global first
    global action
    action = 'subtraction'
    first = e.get()
    e.delete(0, 'end')


def multiply():
    global first
    global action
    action = 'multiplication'
    first = e.get()
    e.delete(0, 'end')


def divide():
    global first
    global action
    action = 'division'
    first = e.get()
    e.delete(0, 'end')


def result():
    global second
    second = e.get()
    e.delete(0, 'end')
    if action == 'addition':
        e.insert(0, int(first) + int(second))
    if action == 'subtraction':
        e.insert(0, int(first) - int(second))
    if action == 'multiplication':
        e.insert(0, int(first) * int(second))
    if action == 'division':
        e.insert(0, int(first) / int(second))


def clear():
    e.delete(0, 'end')


win = tk.Tk()
win.title('Calculator')
win.geometry('250x350')

e = tk.Entry(win, text='', justify='right', bg='#e6f7ff', font=('Helvatical bold', 20))
e.grid(column=0, columnspan=4, row=0, sticky='NSEW')

b1 = tk.Button(win, text='1', bg='#b3e6ff', activeforeground='#cccccc',
               command=lambda: click(1))
b1.grid(column=0, row=2, sticky='NSEW')

b2 = tk.Button(win, text='2', bg='#b3e6ff', activeforeground='#cccccc',
               command=lambda: click(2))
b2.grid(column=1, row=2, sticky='NSEW')

b3 = tk.Button(win, text='3', bg='#b3e6ff', activeforeground='#cccccc',
               command=lambda: click(3))
b3.grid(column=2, row=2, sticky='NSEW')

b4 = tk.Button(win, text='4', bg='#b3e6ff', activeforeground='#cccccc',
               command=lambda: click(4))
b4.grid(column=0, row=3, sticky='NSEW')

b5 = tk.Button(win, text='5', bg='#b3e6ff', activeforeground='#cccccc',
               command=lambda: click(5))
b5.grid(column=1, row=3, sticky='NSEW')

b6 = tk.Button(win, text='6', bg='#b3e6ff', activeforeground='#cccccc',
               command=lambda: click(6))
b6.grid(column=2, row=3, sticky='NSEW')

b7 = tk.Button(win, text='7', bg='#b3e6ff', activeforeground='#cccccc',
               command=lambda: click(7))
b7.grid(column=0, row=4, sticky='NSEW')

b8 = tk.Button(win, text='8', bg='#b3e6ff', activeforeground='#cccccc',
               command=lambda: click(8))
b8.grid(column=1, row=4, sticky='NSEW')

b9 = tk.Button(win, text='9', bg='#b3e6ff', activeforeground='#cccccc',
               command=lambda: click(9))
b9.grid(column=2, row=4, sticky='NSEW')

b0 = tk.Button(win, text='0', bg='#b3e6ff', activeforeground='#cccccc',
               command=lambda: click(0))
b0.grid(column=0, columnspan=3, row=5, sticky='NSEW')

plus = tk.Button(win, text='+', bg='#66ccff', activeforeground='#cccccc', bd=4,
                 command=add)
plus.grid(column=3, row=2, rowspan=2, sticky='NSEW')

minus = tk.Button(win, text='-', bg='#66ccff', activeforeground='#cccccc', bd=4,
                  command=sub)
minus.grid(column=3, row=1, sticky='NSEW')

mult = tk.Button(win, text='×', bg='#66ccff', activeforeground='#cccccc', bd=4,
                 command=multiply)
mult.grid(column=2, row=1, sticky='NSEW')

div = tk.Button(win, text='÷', bg='#66ccff', activeforeground='#cccccc', bd=4,
                command=divide)
div.grid(column=1, row=1, sticky='NSEW')

equal = tk.Button(win, text='=', bg='#66ccff', activeforeground='#cccccc', bd=4,
                  command=result)
equal.grid(column=3, row=4, rowspan=2, sticky='NSEW')

c = tk.Button(win, text='C', bg='#66ccff', activeforeground='#cccccc', bd=4,
              command=clear)
c.grid(column=0, row=1, sticky='NSEW')

win.grid_columnconfigure(0, weight=1)
win.grid_columnconfigure(1, weight=1)
win.grid_columnconfigure(2, weight=1)
win.grid_columnconfigure(3, weight=1)
win.grid_rowconfigure(0, weight=2)
win.grid_rowconfigure(1, weight=1)
win.grid_rowconfigure(2, weight=1)
win.grid_rowconfigure(3, weight=1)
win.grid_rowconfigure(4, weight=1)
win.grid_rowconfigure(5, weight=1)

tk.mainloop()
