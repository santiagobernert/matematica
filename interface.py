from tkinter import *
from grapher import graph

#from functions import Rational, Irrational, Polinomical

class Menu:
    def __init__(self, window):
        self.window = window
        self.function_type = None

        window.title("FunctionSolver")
        window.geometry('800x600')
        window.resizable(width=False, height=False)

        root = Frame(window)
        root.place(x=0,y=0,width=800,height=600)
        root.config(bg='#121212')

#       TITLE

        titulo = Label(root)
        titulo.config(bg='#121212', fg='#f2f2f2', justify=CENTER, font=('Helvetica', '24', 'bold'))
        titulo.config(text='FunctionSolver')
        titulo.place(x=280, y=35)

        labelEnterFunction = Label(root)
        labelEnterFunction.config(bg='#121212', fg='#f2f2f2', justify=LEFT, font=('Helvetica', '16'))
        labelEnterFunction.config(text='Enter function:')
        labelEnterFunction.place(x=85, y=105)

        labelFX = Label(root)
        labelFX.config(bg='#121212', fg='#f2f2f2', justify=LEFT, font=('Helvetica', '16'))
        labelFX.config(text='f(x) = ')
        labelFX.place(x=85, y=145)

        entry = Entry(root)
        entry.config(bg='#f2f2f2', fg='#121212', justify=LEFT, font=('Helvetica', '16'), width=40)
        entry.place(x=150, y=145)

        def changeText():
            function.set('f(x) = ' + entry.get())

        change = Button(root)
        change.config(bg='#f2f2f2', fg='#121212', justify=LEFT, font=('Helvetica', '16'), command=changeText)
        change.config(text='Change')
        change.place(x=550, y=145)

        function = StringVar(value=f'f(x) = {entry.get()}')

        functionLabel = Label(root)
        functionLabel.config(bg='#121212', fg='#f2f2f2', justify=LEFT, font=('Helvetica', '16'))
        functionLabel.config(textvariable=function)
        functionLabel.place(x=85, y=180)

        graphBtn = Button(root)
        graphBtn.config(bg='#f2f2f2', fg='#121212', justify=LEFT, font=('Helvetica', '16'), command=lambda:graph(entry.get()))
        graphBtn.config(text='Graph')
        graphBtn.place(x=85, y=240)




if __name__ == "__main__":
    tk = Tk()
    menu = Menu(tk)
    tk.mainloop()


    