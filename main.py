import tkinter as tk


def click(number):
    if text3.get() == '  ':
        text1.set('')
        text2.set('')
        text3.set('')
        if number == 1:
            text2.set(text2.get() + '1')
        if number == 2:
            text2.set(text2.get() + '2')
        if number == 3:
            text2.set(text2.get() + '3')
        if number == 4:
            text2.set(text2.get() + '4')
        if number == 5:
            text2.set(text2.get() + '5')
        if number == 6:
            text2.set(text2.get() + '6')
        if number == 7:
            text2.set(text2.get() + '7')
        if number == 8:
            text2.set(text2.get() + '8')
        if number == 9:
            text2.set(text2.get() + '9')
        if number == 0:
            text2.set(text2.get() + '0')
    else:
        if number == 1:
            text2.set(text2.get() + '1')
        if number == 2:
            text2.set(text2.get() + '2')
        if number == 3:
            text2.set(text2.get() + '3')
        if number == 4:
            text2.set(text2.get() + '4')
        if number == 5:
            text2.set(text2.get() + '5')
        if number == 6:
            text2.set(text2.get() + '6')
        if number == 7:
            text2.set(text2.get() + '7')
        if number == 8:
            text2.set(text2.get() + '8')
        if number == 9:
            text2.set(text2.get() + '9')
        if number == 0:
            text2.set(text2.get() + '0')


def add():
    global first
    global action
    action = 'addition'
    first = text2.get()
    text1.set(str(first) + ' + ')
    text2.set('')


def sub():
    global first
    global action
    action = 'subtraction'
    first = text2.get()
    text1.set(str(first) + ' - ')
    text2.set('')


def multiply():
    global first
    global action
    action = 'multiplication'
    first = text2.get()
    text1.set(str(first) + ' × ')
    text2.set('')


def divide():
    global first
    global action
    action = 'division'
    first = text2.get()
    text1.set(str(first) + ' ÷ ')
    text2.set('')


def result():
    global second
    second = text2.get()
    text1.set(text1.get() + str(second) + ' = ')
    text2.set('')
    if action == 'addition':
        text2.set(int(first) + int(second))
    if action == 'subtraction':
        text2.set(int(first) - int(second))
    if action == 'multiplication':
        text2.set(int(first) * int(second))
    if action == 'division':
        text2.set(int(first) / int(second))
        last = text2.get()
        if last[-1] == '0':
            text2.set(int(float(last)))
        else:
            text2.set(round(float(last), 2))
    text3.set('  ')


def clear():
    text1.set('')
    text2.set('')


win = tk.Tk()
win.title('Calculator')
win.geometry('250x350')

text1 = tk.StringVar()
text2 = tk.StringVar()
text3 = tk.StringVar()

l1 = tk.Label(win, textvariable=text1, anchor='ne', bg='#e6f7ff', font=('Helvatical bold', 10))
l1.grid(column=0, columnspan=4, row=0, sticky='NSEW')

l2 = tk.Label(win, textvariable=text2, anchor='se', bg='#e6f7ff', font=('Helvatical bold', 30))
l2.grid(column=0, columnspan=4, row=1, sticky='NSEW')

l3 = tk.Label(win, textvariable=text3, anchor='se', bg='#e6f7ff', font=('Helvatical bold', 1))
l3.grid(column=0, columnspan=4, row=2, sticky='NSEW')

# 0-9 buttons

b1 = tk.Button(win, text='1', bg='#b3e6ff', activeforeground='#cccccc',
               command=lambda: click(1))
b1.grid(column=0, row=4, sticky='NSEW')

b2 = tk.Button(win, text='2', bg='#b3e6ff', activeforeground='#cccccc',
               command=lambda: click(2))
b2.grid(column=1, row=4, sticky='NSEW')

b3 = tk.Button(win, text='3', bg='#b3e6ff', activeforeground='#cccccc',
               command=lambda: click(3))
b3.grid(column=2, row=4, sticky='NSEW')

b4 = tk.Button(win, text='4', bg='#b3e6ff', activeforeground='#cccccc',
               command=lambda: click(4))
b4.grid(column=0, row=5, sticky='NSEW')

b5 = tk.Button(win, text='5', bg='#b3e6ff', activeforeground='#cccccc',
               command=lambda: click(5))
b5.grid(column=1, row=5, sticky='NSEW')

b6 = tk.Button(win, text='6', bg='#b3e6ff', activeforeground='#cccccc',
               command=lambda: click(6))
b6.grid(column=2, row=5, sticky='NSEW')

b7 = tk.Button(win, text='7', bg='#b3e6ff', activeforeground='#cccccc',
               command=lambda: click(7))
b7.grid(column=0, row=6, sticky='NSEW')

b8 = tk.Button(win, text='8', bg='#b3e6ff', activeforeground='#cccccc',
               command=lambda: click(8))
b8.grid(column=1, row=6, sticky='NSEW')

b9 = tk.Button(win, text='9', bg='#b3e6ff', activeforeground='#cccccc',
               command=lambda: click(9))
b9.grid(column=2, row=6, sticky='NSEW')

b0 = tk.Button(win, text='0', bg='#b3e6ff', activeforeground='#cccccc',
               command=lambda: click(0))
b0.grid(column=0, columnspan=3, row=7, sticky='NSEW')

# action buttons

plus = tk.Button(win, text='+', bg='#66ccff', activeforeground='#cccccc', bd=4,
                 command=add)
plus.grid(column=3, row=4, rowspan=2, sticky='NSEW')

minus = tk.Button(win, text='-', bg='#66ccff', activeforeground='#cccccc', bd=4,
                  command=sub)
minus.grid(column=3, row=3, sticky='NSEW')

mult = tk.Button(win, text='×', bg='#66ccff', activeforeground='#cccccc', bd=4,
                 command=multiply)
mult.grid(column=2, row=3, sticky='NSEW')

div = tk.Button(win, text='÷', bg='#66ccff', activeforeground='#cccccc', bd=4,
                command=divide)
div.grid(column=1, row=3, sticky='NSEW')

equal = tk.Button(win, text='=', bg='#66ccff', activeforeground='#cccccc', bd=4,
                  command=result)
equal.grid(column=3, row=6, rowspan=2, sticky='NSEW')

c = tk.Button(win, text='C', bg='#66ccff', activeforeground='#cccccc', bd=4,
              command=clear)
c.grid(column=0, row=3, sticky='NSEW')

win.grid_columnconfigure(0, weight=2)
win.grid_columnconfigure(1, weight=2)
win.grid_columnconfigure(2, weight=2)
win.grid_columnconfigure(3, weight=2)
win.grid_rowconfigure(0, weight=0)
win.grid_rowconfigure(1, weight=0)
win.grid_rowconfigure(2, weight=0)
win.grid_rowconfigure(3, weight=2)
win.grid_rowconfigure(4, weight=2)
win.grid_rowconfigure(5, weight=2)
win.grid_rowconfigure(6, weight=2)
win.grid_rowconfigure(7, weight=2)

tk.mainloop()
