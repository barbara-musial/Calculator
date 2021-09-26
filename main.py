import tkinter as tk

win = tk.Tk()
win.title('Calculator')
win.geometry('250x350')

label = tk.Label(win)
label.grid(column=0, columnspan=4, row=0, sticky='NSEW')

b1 = tk.Button(win, text='1')
b1.grid(column=0, row=2, sticky='NSEW')

b2 = tk.Button(win, text='2')
b2.grid(column=1, row=2, sticky='NSEW')

b3 = tk.Button(win, text='3')
b3.grid(column=2, row=2, sticky='NSEW')

b4 = tk.Button(win, text='4')
b4.grid(column=0, row=3, sticky='NSEW')

b5 = tk.Button(win, text='5')
b5.grid(column=1, row=3, sticky='NSEW')

b6 = tk.Button(win, text='6')
b6.grid(column=2, row=3, sticky='NSEW')

b7 = tk.Button(win, text='7')
b7.grid(column=0, row=4, sticky='NSEW')

b8 = tk.Button(win, text='8')
b8.grid(column=1, row=4, sticky='NSEW')

b9 = tk.Button(win, text='9')
b9.grid(column=2, row=4, sticky='NSEW')

b0 = tk.Button(win, text='0')
b0.grid(column=0, columnspan=3, row=5, sticky='NSEW')

plus = tk.Button(win, text='+')
plus.grid(column=3, row=2, rowspan=2, sticky='NSEW')

minus = tk.Button(win, text='-')
minus.grid(column=3, row=1, sticky='NSEW')

multiply = tk.Button(win, text='×')
multiply.grid(column=2, row=1, sticky='NSEW')

divide = tk.Button(win, text='÷')
divide.grid(column=1, row=1, sticky='NSEW')

equal = tk.Button(win, text='=')
equal.grid(column=3, row=4, rowspan=2, sticky='NSEW')

c = tk.Button(win, text='C')
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
