from tkinter import *

from .function import Function
from .grapher import graph

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

        value_a = StringVar(value='a = ')
        value_b = StringVar(value='b = ')
        value_c = StringVar(value='c = ')
        value_d = StringVar(value='d = ')
        value_n1 = StringVar(value='n1 = ')
        value_n2 = StringVar(value='n2 = ')
        value_n3 = StringVar(value='n3 = ')
        value_n4 = StringVar(value='n4 = ')
        value_o1 = StringVar(value='o1 = ')
        value_o2 = StringVar(value='o2 = ')
        value_o3 = StringVar(value='o3 = ')

        func = StringVar(value=f'f(x) = {value_a.get()}x^{value_n1.get()} + {value_b.get()}x^{value_n2.get()} + {value_c.get()}x^{value_n3.get()} + {value_d.get()}x^{value_n4.get()}')
        function = Function(value_a.get(), value_n1.get(), value_o1.get(),  value_b.get(), value_n2.get(), value_o2.get(), value_c.get(), value_n3.get(), value_o3.get(), value_d.get(), value_n4.get())

        def changeText(va, vb, vc, vd):
            va.set('f(x) = ' + entrya.get())
            vb.set('f(x) = ' + entrya.get())
            vc.set('f(x) = ' + entrya.get())
            vd.set('f(x) = ' + entrya.get())



        change = Button(root)
        change.config(bg='#f2f2f2', fg='#121212', justify=LEFT, font=('Helvetica', '16'), command=changeText)
        change.config(text='Change')
        change.place(x=450, y=240)

        functionLabel = Label(root)
        functionLabel.config(bg='#121212', fg='#f2f2f2', justify=LEFT, font=('Helvetica', '16'))
        functionLabel.config(textvariable=func)
        functionLabel.place(x=150, y=340)

        graphBtn = Button(root)
        graphBtn.config(bg='#f2f2f2', fg='#121212', justify=LEFT, font=('Helvetica', '16'), command=lambda:graph(function))
        graphBtn.config(text='Graph')
        graphBtn.place(x=450, y=390)