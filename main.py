import tkinter as tk

BACK_BUTTON_COLOR = '#cccccc'
NUMBER_BUTTON_COLOR = '#b3e6ff'
ACTION_BUTTON_COLOR = '#66ccff'
CENTER = 'NSEW'

win = tk.Tk()
win.title('Calculator')
win.geometry('250x350')

text1 = tk.StringVar()
text2 = tk.StringVar()
text3 = tk.StringVar()


def logic(number):
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


def click(number):
    if text3.get() == '  ':
        text1.set('')
        text2.set('')
        text3.set('')
        logic(number)
    else:
        logic(number)


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
    if first != '' and second != '':
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


def numberButton(x):
    return tk.Button(win, text=x, bg=NUMBER_BUTTON_COLOR, activeforeground=BACK_BUTTON_COLOR, command=lambda: click(x))


def actionButton(sign, function):
    return tk.Button(win, text=sign, bg=ACTION_BUTTON_COLOR, activeforeground=BACK_BUTTON_COLOR, bd=4,
                     command=function)


l1 = tk.Label(win, textvariable=text1, anchor='ne', bg=NUMBER_BUTTON_COLOR, font=('Helvatical bold', 10))
l1.grid(column=0, columnspan=4, row=0, sticky=CENTER)

l2 = tk.Label(win, textvariable=text2, anchor='se', bg=NUMBER_BUTTON_COLOR, font=('Helvatical bold', 30))
l2.grid(column=0, columnspan=4, row=1, sticky=CENTER)

l3 = tk.Label(win, textvariable=text3, anchor='se', bg=NUMBER_BUTTON_COLOR, font=('Helvatical bold', 1))
l3.grid(column=0, columnspan=4, row=2, sticky=CENTER)

# 0-9 buttons

b1 = numberButton(1)
b1.grid(column=0, row=4, sticky=CENTER)

b2 = numberButton(2)
b2.grid(column=1, row=4, sticky=CENTER)

b3 = numberButton(3)
b3.grid(column=2, row=4, sticky=CENTER)

b4 = numberButton(4)
b4.grid(column=0, row=5, sticky=CENTER)

b5 = numberButton(5)
b5.grid(column=1, row=5, sticky=CENTER)

b6 = numberButton(6)
b6.grid(column=2, row=5, sticky=CENTER)

b7 = numberButton(7)
b7.grid(column=0, row=6, sticky=CENTER)

b8 = numberButton(8)
b8.grid(column=1, row=6, sticky=CENTER)

b9 = numberButton(9)
b9.grid(column=2, row=6, sticky=CENTER)

b0 = numberButton(0)
b0.grid(column=0, columnspan=3, row=7, sticky=CENTER)

# action buttons

plus = actionButton('+', lambda: add())
plus.grid(column=3, row=4, rowspan=2, sticky=CENTER)

minus = actionButton('-', lambda: sub())
minus.grid(column=3, row=3, sticky=CENTER)

mult = actionButton('×', lambda: multiply())
mult.grid(column=2, row=3, sticky=CENTER)

div = actionButton('÷', lambda: divide())
div.grid(column=1, row=3, sticky=CENTER)

equal = actionButton('=', lambda: result())
equal.grid(column=3, row=6, rowspan=2, sticky=CENTER)

c = actionButton('C', lambda: clear())
c.grid(column=0, row=3, sticky=CENTER)

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
