from tkinter import *
from . import grapher as g

class Rational:
    def __init__(self, root):
        fromula = Label(root)
        fromula.config(bg='#121212', fg='#f2f2f2', justify=LEFT, font=('Helvetica', '16'))
        fromula.config(text='Constant function formula\n f(x) = a')
        fromula.place(x=85, y=140)
        valueLabel = Label(root)
        valueLabel.config(bg='#121212', fg='#f2f2f2', justify=LEFT, font=('Helvetica', '16'))
        valueLabel.config(text='a =')
        valueLabel.place(x=85, y=240)

 
        entry = Entry(root)
        entry.config(bg='#f2f2f2', fg='#121212', justify=LEFT, font=('Helvetica', '16'))
        entry.place(x=120, y=240)

        value = StringVar(value='f(x) = ')
        def changeText():
            value.set('f(x) = ' + entry.get())



        change = Button(root)
        change.config(bg='#f2f2f2', fg='#121212', justify=LEFT, font=('Helvetica', '16'), command=changeText)
        change.config(text='Change')
        change.place(x=450, y=240)

        function = Label(root)
        function.config(bg='#121212', fg='#f2f2f2', justify=LEFT, font=('Helvetica', '16'))
        function.config(textvariable=value)
        function.place(x=150, y=340)

        graphBtn = Button(root)
        graphBtn.config(bg='#f2f2f2', fg='#121212', justify=LEFT, font=('Helvetica', '16'), command=lambda:g.graph(value.get()))
        graphBtn.config(text='Graph')
        graphBtn.place(x=450, y=390)