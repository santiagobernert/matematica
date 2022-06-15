from tkinter import *
from . import grapher as g

class Polinomical:
    def __init__(self, root):
        fromula = Label(root)
        fromula.config(bg='#121212', fg='#f2f2f2', justify=LEFT, font=('Helvetica', '16'))
        fromula.config(text='Polinomical function formula\n f(x) = ax^3+bx^2+cx+d.')
        fromula.place(x=85, y=140)

        valueLabel = Label(root)
        valueLabel.config(bg='#121212', fg='#f2f2f2', justify=LEFT, font=('Helvetica', '16'))
        valueLabel.config(text='a =')
        valueLabel.place(x=85, y=240)

        valueLabel = Label(root)
        valueLabel.config(bg='#121212', fg='#f2f2f2', justify=LEFT, font=('Helvetica', '16'))
        valueLabel.config(text='b =')
        valueLabel.place(x=85, y=240)

        valueLabel = Label(root)
        valueLabel.config(bg='#121212', fg='#f2f2f2', justify=LEFT, font=('Helvetica', '16'))
        valueLabel.config(text='c =')
        valueLabel.place(x=85, y=240)

        valueLabel = Label(root)
        valueLabel.config(bg='#121212', fg='#f2f2f2', justify=LEFT, font=('Helvetica', '16'))
        valueLabel.config(text='d =')
        valueLabel.place(x=85, y=240)

 
        entrya = Entry(root)
        entrya.config(bg='#f2f2f2', fg='#121212', justify=LEFT, font=('Helvetica', '16'))
        entrya.place(x=120, y=240)
 
        entryb = Entry(root)
        entryb.config(bg='#f2f2f2', fg='#121212', justify=LEFT, font=('Helvetica', '16'))
        entryb.place(x=120, y=240)
 
        entryc = Entry(root)
        entryc.config(bg='#f2f2f2', fg='#121212', justify=LEFT, font=('Helvetica', '16'))
        entryc.place(x=120, y=240)
 
        entryd = Entry(root)
        entryd.config(bg='#f2f2f2', fg='#121212', justify=LEFT, font=('Helvetica', '16'))
        entryd.place(x=120, y=240)

        value_a = StringVar(value='f(x) = ')
        value_b = StringVar(value='f(x) = ')
        value_c = StringVar(value='f(x) = ')
        value_d = StringVar(value='f(x) = ')
        
        def changeText(va, vb, vc, vd):
            va.set('f(x) = ' + entrya.get())
            vb.set('f(x) = ' + entrya.get())
            vc.set('f(x) = ' + entrya.get())
            vd.set('f(x) = ' + entrya.get())



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